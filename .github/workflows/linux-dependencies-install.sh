#!/bin/bash

set -e

apt update

# Install sys tools
apt install -y libgirepository-2.0-dev gcc libcairo2-dev python3-cairo-dev pkg-config python3-dev python3-setuptools libevent-dev build-essential gir1.2-gtk-4.0
