#!/bin/sh
apk update
apk upgrade 

# apk add python 
apk add python3
apk add libxml2

pip3 install yagmail
apkk add python3-pip
# apk add python-pip

apk add git 
pip3 install yagmail 
pip install yagmail 

cd ~
git clone https://github.com/bagarrattaa/gmail-bomber-client
