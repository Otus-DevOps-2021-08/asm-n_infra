#!/bin/bash -x

INSTANCE_NAME="reddit-app"
IMAGE_FAMILY="reddit-base"

yc compute instance create \
  --name ${INSTANCE_NAME} \
  --hostname ${INSTANCE_NAME} \
  --memory=4 \
  --create-boot-disk image-family=${IMAGE_FAMILY} \
  --network-interface subnet-name=default-ru-central1-a,nat-ip-version=ipv4 \
  --metadata serial-port-enable=1 \
  --metadata-from-file user-data=./user-data.yml
