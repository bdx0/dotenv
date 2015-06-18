:: %~dp0

set PATH=C:\tools\cygwin\bin;D:\tools\go;%~dp0;%~dp0scripts;%PATH%
set PATH=D:\tools\LLVM\bin;D:\tools\LLVM\msbuild-bin;%PATH%

set HOME=D:/dbduy0206/dbd-home

set NDK_ROOT=D:\tools\android-ndk
set SDK_ROOT=D:\tools\android-sdk
set PATH=%NDK_ROOT%;%SDK_ROOT%\platform-tools;%SDK_ROOT%\tools;%PATH%

:: set path for python
set PYTHON=D:\tools\python2
set PATH=%PYTHON%;%PYTHON%\Scripts;%PATH%

start "" /MAX "atom" --include-deprecated-apis
:: D:\tools\eclipse-4.4\eclipse.exe --data D:\workspace-dbd
start "" /MAX "D:\tools\eclipse-android\eclipse.exe" -data D:\workspace
