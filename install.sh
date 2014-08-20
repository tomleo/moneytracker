
# NOTE: This is not a functioning bash script
# Below are basically the required steps to get a working environment for the
# project

#!/usr/bin/env bash
export DEBIAN_FRONTEND=noninteractive

sudo cp /vagrant/moneytraker/pgdg.list /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get upgrade


sudo apt-get install build-essential
sudo apt-get install libncurses5-dev libncursesw5-dev libreadline6-dev
sudo apt-get install libdb5.1-dev libgdbm-dev libsqlite3-dev libssl-dev
sudo apt-get install libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

cd /vagrant/Python-3.4.1
tar xvfJ Python-3.4.1.tar.xz
./configure
make
sudo make install

sudo apt-get install flex bison libreadline6-dev zlib1g-dev libossp-uuid-dev wget ca-certificates vim
sudo apt-get install postgresql-9.3
sudo apt-get install postgresql-contrib postgresql-9.3-postgis-2.1 postgresql-9.3-postgis-scripts
sudo apt-get install libpq-dev

cd /vagrant/moneytraker/

pyvenv-3.4 venv
source env/bin/activate
pip install https://www.djangoproject.com/download/1.7c2/tarball/
pip install -r requirements.txt

sudo mkdir /var/log/moneytraker
sudo chown -R vagrant:vagrant /var/log/moneytraker/

#NOTE: postgres=# lines are within psql cli
sudo -u postgres createdb moneytraker
sudo -u postgres createuser vagrant
sudo -u postgres psql
postgres=# GRANT ALL PRIVILEGES ON DATABASE moneytraker To vagrant;
postgres=# ALTER USER vagrant WITH PASSWORD 'thomas';
postgres=# \q


