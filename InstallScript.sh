#!/bin/bash

set -e

apt-get update
apt-get install -y python-pip python-dev

pip install Django==1.8.3
pip install django-registration-redux==1.2
pip install django-social-auth==0.7.28