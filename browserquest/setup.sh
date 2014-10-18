#!/bin/bash

apt-get update
apt-get install -y nginx nodejs

# have nodejs package provide /usr/bin/node (required for some scripts)
sudo update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

# configure settings for client js app
echo '{ "host": "192.168.33.10/ws/", "port": 80 }' > /vagrant/src/client/config/config_build.json

pushd /vagrant/src/bin && ./build.sh
popd

sudo ln -s /vagrant/src/client-build /srv/browserquest

sudo ln -s /vagrant/nginx-browserquest.conf /etc/nginx/sites-available/browserquest
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/browserquest /etc/nginx/sites-enabled/browserquest
sudo service nginx restart
