import sys
import contextlib
import unittest
import os
import time

def _id(obj):
    return obj

def cpython_only(test):
    """
    Decorator for tests only applicable on CPython.
    """
    return impl_detail(cpython=True)(test)

def impl_detail(msg=None, **guards):
    if check_impl_detail(**guards):
        return _id
    if msg is None:
        guardnames, default = _parse_guards(guards)
        if default:
            msg = "implementation detail not available on {0}"
        else:
            msg = "implementation detail specific to {0}"
        guardnames = sorted(guardnames.keys())
        msg = msg.format(' or '.join(guardnames))
    return unittest.skip(msg)

def _parse_guards(guards):
    # Returns a tuple ({platform_name: run_me}, default_value)
    if not guards:
        return ({'cpython': True}, False)
    is_true = list(guards.values())[0]
    assert list(guards.values()) == [is_true] * len(guards)   # all True or all False
    return (guards, not is_true)

# Use the following check to guard CPython's implementation-specific tests --
# or to run them only on the implementation(s) guarded by the arguments.
def check_impl_detail(**guards):
    """This function returns True or False depending on the host platform.
       Examples:
          if check_impl_detail():               # only on CPython (default)
          if check_impl_detail(jython=True):    # only on Jython
          if check_impl_detail(cpython=False):  # everywhere except on CPython
    """
    guards, default = _parse_guards(guards)
    return guards.get(sys.implementation.name, default)

@contextlib.contextmanager
def swap_attr(obj, attr, new_val):
    """Temporary swap out an attribute with a new object.

    Usage:
        with swap_attr(obj, "attr", 5):
            ...

        This will set obj.attr to 5 for the duration of the with: block,
        restoring the old value at the end of the block. If `attr` doesn't
        exist on `obj`, it will be created and then deleted at the end of the
        block.

        The old value (or None if it doesn't exist) will be assigned to the
        target of the "as" clause, if there is one.
    """
    if hasattr(obj, attr):
        real_val = getattr(obj, attr)
        setattr(obj, attr, new_val)
        try:
            yield real_val
        finally:
            setattr(obj, attr, real_val)
    else:
        setattr(obj, attr, new_val)
        try:
            yield
        finally:
            if hasattr(obj, attr):
                delattr(obj, attr)

MS_WINDOWS = (sys.platform == 'win32')
is_emscripten = sys.platform == "emscripten"
is_android = sys.platform == "android"
is_apple_mobile = sys.platform in {"ios", "tvos", "watchos"}
is_apple = is_apple_mobile or sys.platform == "darwin"
is_wasi = sys.platform == "wasi"

has_fork_support = hasattr(os, "fork") and not (
    # WASM and Apple mobile platforms do not support subprocesses.
    is_emscripten
    or is_wasi
    or is_apple_mobile

    # Although Android supports fork, it's unsafe to call it from Python because
    # all Android apps are multi-threaded.
    or is_android
)

def requires_fork():
    return unittest.skipUnless(has_fork_support, "requires working os.fork()")

has_subprocess_support = not (
    # WASM and Apple mobile platforms do not support subprocesses.
    is_emscripten
    or is_wasi
    or is_apple_mobile

    # Although Android supports subproceses, they're almost never useful in
    # practice (see PEP 738). And most of the tests that use them are calling
    # sys.executable, which won't work when Python is embedded in an Android app.
    or is_android
)

def requires_subprocess():
    """Used for subprocess, os.spawn calls, fd inheritance"""
    return unittest.skipUnless(has_subprocess_support, "requires subprocess support")

WINDOWS_STATUS = {
    0xC0000005: "STATUS_ACCESS_VIOLATION",
    0xC00000FD: "STATUS_STACK_OVERFLOW",
    0xC000013A: "STATUS_CONTROL_C_EXIT",
}

def get_signal_name(exitcode):
    import signal

    if exitcode < 0:
        signum = -exitcode
        try:
            return signal.Signals(signum).name
        except ValueError:
            pass

    # Shell exit code (ex: WASI build)
    if 128 < exitcode < 256:
        signum = exitcode - 128
        try:
            return signal.Signals(signum).name
        except ValueError:
            pass

    try:
        return WINDOWS_STATUS[exitcode]
    except KeyError:
        pass

    return None


verbose = 1              # Flag set to 0 by regrtest.py

def gc_collect():
    import gc

    gc.collect()
    gc.collect()
    gc.collect()


# Timeout in seconds to detect when a test hangs.
#
# It is long enough to reduce the risk of test failure on the slowest Python
# buildbots. It should not be used to mark a test as failed if the test takes
# "too long". The timeout value depends on the regrtest --timeout command line
# option.
LONG_TIMEOUT = 5 * 60.0


def busy_retry(timeout, err_msg=None, /, *, error=True):
    """
    Run the loop body until "break" stops the loop.

    After *timeout* seconds, raise an AssertionError if *error* is true,
    or just stop if *error is false.

    Example:

        for _ in support.busy_retry(support.SHORT_TIMEOUT):
            if check():
                break

    Example of error=False usage:

        for _ in support.busy_retry(support.SHORT_TIMEOUT, error=False):
            if check():
                break
        else:
            raise RuntimeError('my custom error')

    """
    if timeout <= 0:
        raise ValueError("timeout must be greater than zero")

    start_time = time.monotonic()
    deadline = start_time + timeout

    while True:
        yield

        if time.monotonic() >= deadline:
            break

    if error:
        dt = time.monotonic() - start_time
        msg = f"timeout ({dt:.1f} seconds)"
        if err_msg:
            msg = f"{msg}: {err_msg}"
        raise AssertionError(msg)


def sleeping_retry(timeout, err_msg=None, /,
                     *, init_delay=0.010, max_delay=1.0, error=True):
    """
    Wait strategy that applies exponential backoff.

    Run the loop body until "break" stops the loop. Sleep at each loop
    iteration, but not at the first iteration. The sleep delay is doubled at
    each iteration (up to *max_delay* seconds).

    See busy_retry() documentation for the parameters usage.

    Example raising an exception after SHORT_TIMEOUT seconds:

        for _ in support.sleeping_retry(support.SHORT_TIMEOUT):
            if check():
                break

    Example of error=False usage:

        for _ in support.sleeping_retry(support.SHORT_TIMEOUT, error=False):
            if check():
                break
        else:
            raise RuntimeError('my custom error')
    """

    delay = init_delay
    for _ in busy_retry(timeout, err_msg, error=error):
        yield

        time.sleep(delay)
        delay = min(delay * 2, max_delay)

def _waitstatus_to_exitcode(status):
    if os.WIFEXITED(status):
        return os.WEXITSTATUS(status)
    elif os.WIFSIGNALED(status):
        return -os.WTERMSIG(status)
    else:
        raise ValueError

def wait_process(pid, *, exitcode, timeout=None):
    """
    Wait until process pid completes and check that the process exit code is
    exitcode.

    Raise an AssertionError if the process exit code is not equal to exitcode.

    If the process runs longer than timeout seconds (LONG_TIMEOUT by default),
    kill the process (if signal.SIGKILL is available) and raise an
    AssertionError. The timeout feature is not available on Windows.
    """
    if os.name != "nt":
        import signal

        if timeout is None:
            timeout = LONG_TIMEOUT

        start_time = time.monotonic()
        for _ in sleeping_retry(timeout, error=False):
            pid2, status = os.waitpid(pid, os.WNOHANG)
            if pid2 != 0:
                break
            # rety: the process is still running
        else:
            try:
                os.kill(pid, signal.SIGKILL)
                os.waitpid(pid, 0)
            except OSError:
                # Ignore errors like ChildProcessError or PermissionError
                pass

            dt = time.monotonic() - start_time
            raise AssertionError(f"process {pid} is still running "
                                 f"after {dt:.1f} seconds")
    else:
        # Windows implementation: don't support timeout :-(
        pid2, status = os.waitpid(pid, 0)

    exitcode2 = _waitstatus_to_exitcode(status)
    if exitcode2 != exitcode:
        raise AssertionError(f"process {pid} exited with code {exitcode2}, "
                             f"but exit code {exitcode} is expected")

    # sanity check: it should not fail in practice
    if pid2 != pid:
        raise AssertionError(f"pid {pid2} != pid {pid}")
