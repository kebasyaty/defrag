#!/bin/bash

set -e

apt update

# Install sys tools
apt install -y libgirepository-2.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0
