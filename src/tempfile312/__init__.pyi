"""
This file is copied from typeshed/stdlib/tempfile.pyi.

The "typeshed" project is licensed under the terms of the Apache license, as
reproduced below.

= = = = =

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import io
from os import PathLike
import sys
from _typeshed import (
    BytesPath,
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
    ReadableBuffer,
    StrPath,
    WriteableBuffer,
)
from collections.abc import Iterable, Iterator
from types import TracebackType
from typing import IO, Any, AnyStr, Generic, Literal, overload

if sys.version_info >= (3, 9):
    from types import GenericAlias

GenericPath = AnyStr | PathLike[AnyStr]

__all__ = [
    "NamedTemporaryFile",
    "TemporaryFile",
    "SpooledTemporaryFile",
    "TemporaryDirectory",
    "mkstemp",
    "mkdtemp",
    "mktemp",
    "TMP_MAX",
    "gettempprefix",
    "tempdir",
    "gettempdir",
    "gettempprefixb",
    "gettempdirb",
]

# global variables
TMP_MAX: int
tempdir: str | None
template: str

@overload
def NamedTemporaryFile(
    mode: OpenTextMode,
    buffering: int = -1,
    encoding: str | None = None,
    newline: str | None = None,
    suffix: AnyStr | None = None,
    prefix: AnyStr | None = None,
    dir: GenericPath[AnyStr] | None = None,
    delete: bool = True,
    *,
    errors: str | None = None,
    delete_on_close: bool = True,
) -> _TemporaryFileWrapper[str]: ...
@overload
def NamedTemporaryFile(
    mode: OpenBinaryMode = "w+b",
    buffering: int = -1,
    encoding: str | None = None,
    newline: str | None = None,
    suffix: AnyStr | None = None,
    prefix: AnyStr | None = None,
    dir: GenericPath[AnyStr] | None = None,
    delete: bool = True,
    *,
    errors: str | None = None,
    delete_on_close: bool = True,
) -> _TemporaryFileWrapper[bytes]: ...
@overload
def NamedTemporaryFile(
    mode: str = "w+b",
    buffering: int = -1,
    encoding: str | None = None,
    newline: str | None = None,
    suffix: AnyStr | None = None,
    prefix: AnyStr | None = None,
    dir: GenericPath[AnyStr] | None = None,
    delete: bool = True,
    *,
    errors: str | None = None,
    delete_on_close: bool = True,
) -> _TemporaryFileWrapper[Any]: ...


if sys.platform == "win32":
    TemporaryFile = NamedTemporaryFile
else:
    # See the comments for builtins.open() for an explanation of the overloads.
    @overload
    def TemporaryFile(
        mode: OpenTextMode,
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        *,
        errors: str | None = None,
    ) -> io.TextIOWrapper: ...
    @overload
    def TemporaryFile(
        mode: OpenBinaryMode,
        buffering: Literal[0],
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        *,
        errors: str | None = None,
    ) -> io.FileIO: ...
    @overload
    def TemporaryFile(
        *,
        buffering: Literal[0],
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        errors: str | None = None,
    ) -> io.FileIO: ...
    @overload
    def TemporaryFile(
        mode: OpenBinaryModeWriting,
        buffering: Literal[-1, 1] = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        *,
        errors: str | None = None,
    ) -> io.BufferedWriter: ...
    @overload
    def TemporaryFile(
        mode: OpenBinaryModeReading,
        buffering: Literal[-1, 1] = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        *,
        errors: str | None = None,
    ) -> io.BufferedReader: ...
    @overload
    def TemporaryFile(
        mode: OpenBinaryModeUpdating = "w+b",
        buffering: Literal[-1, 1] = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        *,
        errors: str | None = None,
    ) -> io.BufferedRandom: ...
    @overload
    def TemporaryFile(
        mode: str = "w+b",
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: AnyStr | None = None,
        prefix: AnyStr | None = None,
        dir: GenericPath[AnyStr] | None = None,
        *,
        errors: str | None = None,
    ) -> IO[Any]: ...

class _TemporaryFileWrapper(IO[AnyStr]):
    file: IO[AnyStr]  # io.TextIOWrapper, io.BufferedReader or io.BufferedWriter
    name: str
    delete: bool
    def __init__(self, file: IO[AnyStr], name: str, delete: bool = True, delete_on_close: bool = True) -> None: ...

    def __enter__(self) -> "_TemporaryFileWrapper": ...
    def __exit__(self, exc: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def close(self) -> None: ...
    # These methods don't exist directly on this object, but
    # are delegated to the underlying IO object through __getattr__.
    # We need to add them here so that this class is concrete.
    def __iter__(self) -> Iterator[AnyStr]: ...
    # FIXME: __next__ doesn't actually exist on this class and should be removed:
    #        see also https://github.com/python/typeshed/pull/5456#discussion_r633068648
    # >>> import tempfile
    # >>> ntf=tempfile.NamedTemporaryFile()
    # >>> next(ntf)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: '_TemporaryFileWrapper' object is not an iterator
    def __next__(self) -> AnyStr: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> AnyStr: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> AnyStr: ...
    def readlines(self, hint: int = ...) -> list[AnyStr]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int | None = ...) -> int: ...
    def writable(self) -> bool: ...
    @overload
    def write(self: _TemporaryFileWrapper[str], s: str, /) -> int: ...
    @overload
    def write(self: _TemporaryFileWrapper[bytes], s: ReadableBuffer, /) -> int: ...
    @overload
    def write(self, s: AnyStr, /) -> int: ...
    @overload
    def writelines(self: _TemporaryFileWrapper[str], lines: Iterable[str]) -> None: ...
    @overload
    def writelines(self: _TemporaryFileWrapper[bytes], lines: Iterable[ReadableBuffer]) -> None: ...
    @overload
    def writelines(self, lines: Iterable[AnyStr]) -> None: ...
    @property
    def closed(self) -> bool: ...

if sys.version_info >= (3, 11):
    _SpooledTemporaryFileBase = io.IOBase
else:
    _SpooledTemporaryFileBase = object

# It does not actually derive from IO[AnyStr], but it does mostly behave
# like one.
class SpooledTemporaryFile(IO[AnyStr], _SpooledTemporaryFileBase):
    _file: IO[AnyStr]
    @property
    def encoding(self) -> str: ...  # undocumented
    @property
    def newlines(self) -> str | tuple[str, ...] | None: ...  # undocumented
    # bytes needs to go first, as default mode is to open as bytes
    @overload
    def __init__(
        self: SpooledTemporaryFile[bytes],
        max_size: int = 0,
        mode: OpenBinaryMode = "w+b",
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: str | None = None,
        prefix: str | None = None,
        dir: str | None = None,
        *,
        errors: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: SpooledTemporaryFile[str],
        max_size: int,
        mode: OpenTextMode,
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: str | None = None,
        prefix: str | None = None,
        dir: str | None = None,
        *,
        errors: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: SpooledTemporaryFile[str],
        max_size: int = 0,
        *,
        mode: OpenTextMode,
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: str | None = None,
        prefix: str | None = None,
        dir: str | None = None,
        errors: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        max_size: int,
        mode: str,
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: str | None = None,
        prefix: str | None = None,
        dir: str | None = None,
        *,
        errors: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        max_size: int = 0,
        *,
        mode: str,
        buffering: int = -1,
        encoding: str | None = None,
        newline: str | None = None,
        suffix: str | None = None,
        prefix: str | None = None,
        dir: str | None = None,
        errors: str | None = None,
    ) -> None: ...
    @property
    def errors(self) -> str | None: ...
    def rollover(self) -> None: ...
    def __enter__(self) -> "SpooledTemporaryFile": ...
    def __exit__(self, exc: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...
    # These methods are copied from the abstract methods of IO, because
    # SpooledTemporaryFile implements IO.
    # See also https://github.com/python/typeshed/pull/2452#issuecomment-420657918.
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    if sys.version_info >= (3, 11):
        # These three work only if the SpooledTemporaryFile is opened in binary mode,
        # because the underlying object in text mode does not have these methods.
        def read1(self, size: int = ..., /) -> AnyStr: ...
        def readinto(self, b: WriteableBuffer) -> int: ...
        def readinto1(self, b: WriteableBuffer) -> int: ...
        def detach(self) -> io.RawIOBase: ...

    def read(self, n: int = ..., /) -> AnyStr: ...
    def readline(self, limit: int | None = ..., /) -> AnyStr: ...  # type: ignore[override]
    def readlines(self, hint: int = ..., /) -> list[AnyStr]: ...  # type: ignore[override]
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def tell(self) -> int: ...
    if sys.version_info >= (3, 11):
        def truncate(self, size: int | None = None) -> int: ...
    else:
        def truncate(self, size: int | None = None) -> None: ...  # type: ignore[override]

    @overload
    def write(self: SpooledTemporaryFile[str], s: str) -> int: ...
    @overload
    def write(self: SpooledTemporaryFile[bytes], s: ReadableBuffer) -> int: ...
    @overload
    def write(self, s: AnyStr) -> int: ...
    @overload
    def writelines(self: SpooledTemporaryFile[str], iterable: Iterable[str]) -> None: ...
    @overload
    def writelines(self: SpooledTemporaryFile[bytes], iterable: Iterable[ReadableBuffer]) -> None: ...
    @overload
    def writelines(self, iterable: Iterable[AnyStr]) -> None: ...
    def __iter__(self) -> Iterator[AnyStr]: ...  # type: ignore[override]
    # These exist at runtime only on 3.11+.
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...
    def __next__(self) -> AnyStr: ...  # type: ignore[override]
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

class TemporaryDirectory(Generic[AnyStr]):
    name: AnyStr
    @overload
    def __init__(
        self: TemporaryDirectory[str],
        suffix: str | None = None,
        prefix: str | None = None,
        dir: StrPath | None = None,
        ignore_cleanup_errors: bool = False,
        *,
        delete: bool = True,
    ) -> None: ...
    @overload
    def __init__(
        self: TemporaryDirectory[bytes],
        suffix: bytes | None = None,
        prefix: bytes | None = None,
        dir: BytesPath | None = None,
        ignore_cleanup_errors: bool = False,
        *,
        delete: bool = True,
    ) -> None: ...

    def cleanup(self) -> None: ...
    def __enter__(self) -> AnyStr: ...
    def __exit__(self, exc: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

# The overloads overlap, but they should still work fine.
@overload
def mkstemp(
    suffix: str | None = None, prefix: str | None = None, dir: StrPath | None = None, text: bool = False
) -> tuple[int, str]: ...
@overload
def mkstemp(
    suffix: bytes | None = None, prefix: bytes | None = None, dir: BytesPath | None = None, text: bool = False
) -> tuple[int, bytes]: ...

# The overloads overlap, but they should still work fine.
@overload
def mkdtemp(suffix: str | None = None, prefix: str | None = None, dir: StrPath | None = None) -> str: ...
@overload
def mkdtemp(suffix: bytes | None = None, prefix: bytes | None = None, dir: BytesPath | None = None) -> bytes: ...
def mktemp(suffix: str = "", prefix: str = "tmp", dir: StrPath | None = None) -> str: ...
def gettempdirb() -> bytes: ...
def gettempprefixb() -> bytes: ...
def gettempdir() -> str: ...
def gettempprefix() -> str: ...
