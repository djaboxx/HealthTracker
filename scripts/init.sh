#!/bin/bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

apt-get update
apt-get install -y python3 python3-pip wget gnupg mongodb-org

pip3 install jupyter
pip3 install django
pip3 install pymongo pymongo[snappy,gssapi,srv,tls]
pip3 install dnspython
pip3 install mongoengine
pip3 install djongo
