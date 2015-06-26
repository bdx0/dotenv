#!/bin/bash -
OPT_TOOLS_PATH=~/opt/tools
[ -d $OPT_TOOLS_PATH ] || mkdir -p $OPT_TOOLS_PATH

pushd $OPT_TOOLS_PATH

if [ "$1" == "-r"  ]
then
	[ -d eclipse-jee ] && rm -rf eclipse-jee 
	[ -d android-sdk ] && rm -rf android-sdk
	[ -d android-studio ] && rm -rf android-studio
	[ -d android-ndk ] && rm -rf android-ndk	
	[ -d dropbox ] && rm -rf dropbox
	[ -d gnumake ] && rm -rf gnumake
fi
([ -d eclipse-jee ] && echo installed eclipse) || (mkdir eclipse-jee && wget -O- ftp://mirror.cc.columbia.edu/pub/software/eclipse/technology/epp/downloads/release/indigo/SR2/eclipse-jee-indigo-SR2-linux-gtk-x86_64.tar.gz | tar -xz --strip-components=1 -C eclipse-jee)
([ -d android-sdk ] && echo installed android sdk) || (mkdir android-sdk && wget -O- http://dl.google.com/android/android-sdk_r24.0.2-linux.tgz | tar -xz --strip-components=1 -C android-sdk)
([ -d android-studio ] && echo installed android studio) || (wget -O- -O tmp.zip https://dl.google.com/dl/android/studio/ide-zips/1.1.0/android-studio-ide-135.1740770-linux.zip && unzip tmp.zip -d . && rm tmp.zip)
([ -d android-ndk ] && echo installed android ndk) || (wget -O- -O android-ndk.bin  http://dl.google.com/android/ndk/android-ndk-r10d-linux-x86_64.bin  && sh android-ndk.bin && mv android-ndk-r10d android-ndk && rm android-ndk.bin) 
([ -d dropbox ] && echo installed dropbox) || (mkdir dropbox && (wget -O - https://www.dropbox.com/download?plat=lnx.x86_64 | tar -zx --strip-components=1 -C dropbox) && ln -fs ~/.dropbox-dist ./dropbox)
([ -d gnumake ] && echo installed gnumake 3.82) || (mkdir gnumake && (wget -O - http://ftp.gnu.org/gnu/make/make-3.82.tar.gz | tar -zx --strip-components=1 -C gnumake))
popd 
#wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz"


#if [ "$1" == "-r" ]
#then
#	[ -d ~/.dropbox-dist ] && rm -rf ~/.dropbox-dist
#fi 
#cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
