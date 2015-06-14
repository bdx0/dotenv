:: %~dp0

set PATH=C:\tools\cygwin\bin;D:\tools\go;%~dp0;%~dp0scripts;%PATH%
set PATH=D:\tools\LLVM\bin;D:\tools\LLVM\msbuild-bin;%PATH%

set HOME=D:/dbduy0206/dbd-home

set NDK_ROOT=D:\tools\android-ndk
set SDK_ROOT=D:\tools\android-sdk
set PATH=%NDK_ROOT%;%SDK_ROOT%\platform-tools;%SDK_ROOT%\tools;%PATH%

atom --include-deprecated-apis C:\tmp\dotenv
D:\tools\eclipse-4.4\eclipse.exe -d D:\workspace-dbd
D:\tools\eclipse-android\eclipse.exe -d D:\workspace-dbd
