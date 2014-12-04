
# NOTE: This is not a functioning bash script
# Below are basically the required steps to get a working environment for the
# project

#!/usr/bin/env bash
export DEBIAN_FRONTEND=noninteractive

sudo echo 'deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main' >> /etc/apt/sources.list.d/pgdg.list

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

cd /vagrant/mt/

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


##
# Instaslling Nginx & uwsgi
##

sudo apt-get install nginx-full
wget http://projects.unbit.it/downloads/uwsgi-2.0.7.tar.gz
tar xvf uwsgi-2.0.7.tar.gz
source venv/bin/activate
cd uwsgi-2.0.7
python uwsgiconfig.py --build
./uwsgi --http :8000 --chdir /vagrant/mt/ --wsgi-file ./mt/wsgi.py -H /vagrant/venv

sudo chown -R www-data:www-data /var/log/nginx/
sudo /etc/init.d/nginx start
ln -s /etc/nginx/sites-available/moneytracker /etc/nginx/sites-enabled/moneytracker
sudo /etc/init.d/nginx reload


