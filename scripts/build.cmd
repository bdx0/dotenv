
set GOPATH=%~dp0;%GOPATH%

cd src
go get .\...
cd ..
go install main
