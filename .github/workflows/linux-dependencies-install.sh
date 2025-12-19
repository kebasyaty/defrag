#!/bin/bash

set -e

apt update

# Install OS dependencies
apt install -y curl
apt install -y libgirepository-2.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
# Run pre-commit
uv run pre-commit run --all-files
