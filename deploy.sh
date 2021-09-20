#!/bin/bash

if ! git --version > /dev/null; then
  echo "Install git first. Exiting..."
  exit 1
fi

cd ~
git clone -b monolith https://github.com/express42/reddit.git
cd reddit && bundle install
puma -d
