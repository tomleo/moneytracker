unset DJANGO_SETTINGS_MODULE

Installation for Ubuntu 16.04 Failed...

Using `CharField` for points instead of PointField

``` console
sudo apt-get install libreadosm-dev
sudo apt-get install libwxgtk3.0-dev
sudo apt-get install libgif-dev
sudo apt-get install libtiff-dev
sudo apt-get install libgeotiff-dev
sudo apt-get install libwebp-dev
sudo apt-get install libcairo2-dev
sudo apt-get install libcurl4-openssl-dev

wget http://www.gaia-gis.it/gaia-sins/freexl-1.0.4.tar.gz
tar xzvf freexl-1.0.4.tar.gz
cd freexl-1.0.4/
./configure
make
sudo make install

wget http://www.gaia-gis.it/gaia-sins/libspatialite-4.3.0a.tar.gz
tar xzvf libspatialite-4.3.0a.tar.gz
cd libspatialite-4.3.0a/
./configure
make
sudo make install

wget http://www.gaia-gis.it/gaia-sins/spatialite-tools-4.3.0.tar.gz
tar xzvf spatialite-tools-4.3.0.tar.gz
cd spatialite-tools-4.3.0/
./configure
make
sudo make install

wget http://www.gaia-gis.it/gaia-sins/librasterlite2-1.0.0-rc0.tar.gz
tar xzvf librasterlite2-1.0.0-rc0.tar.gz
cd librasterlite2-1.0.0-rc0/
./configure
make
sudo make install
```
