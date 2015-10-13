############################################################
# Dockerfile
# Based on Ubuntu
# This is the Dev Build
############################################################
# Set the base image to Ubuntu
#FROM ubuntu:wily
FROM python:2-onbuild
# Add the application resources URL
#RUN echo "deb http://apt.dockerproject.org/repo/dists/ubuntu-wily/main" > /etc/apt/sources.list

# File Author / Maintainer
MAINTAINER Robert Donovan <admin@mixfin.com>

#run apt-get update
#run apt-get install -y build-essential git
#run apt-get install -y python python-dev python-setuptools libmysqlclient-dev
#run apt-get install -y nginx supervisor
#run easy_install pip

#env PATH /path/to/bin/folder:$PATH

# install uwsgi now because it takes a little while
#run pip install uwsgi

# install nginx
#run apt-get install -y software-properties-common python-software-properties
#run apt-get update
#run add-apt-repository -y ppa:nginx/stable
#run apt-get install -y sqlite3

# install our code
#add . /home/docker/code/

# setup all the configfiles
#run echo "daemon off;" >> /etc/nginx/nginx.conf
#run rm /etc/nginx/sites-enabled/default
#run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
#run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
#run pip install -r /home/docker/code/app/requirements.txt
run pip install -r /home/docker/app/requirements.txt

#ADD run.sh run.sh

#run chmod +X run.sh

#expose 80
#cmd ./run.sh
#cmd ["supervisord", "-n"]
