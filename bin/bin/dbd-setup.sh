#!/bin/bash -
wget -q0- http://dl.google.com/android/android-sdk_r24.0.2-linux.tgz | tar xvz -C android-sdk
wget -qO- -O tmp.zip https://dl.google.com/dl/android/studio/ide-zips/1.1.0/android-studio-ide-135.1740770-linux.zip && unzip tmp.zip && rm tmp.zip
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
