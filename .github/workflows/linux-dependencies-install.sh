#!/bin/bash

set -e

apt update

apt install -y sudo

sudo apt -y update
sudo apt -y upgrade

# Install sys tools
sudo apt install -y libgirepository-2.0-dev gcc libcairo2-dev python3-cairo-dev pkg-config python3-dev python3-setuptools libevent-dev build-essential gir1.2-gtk-4.0
