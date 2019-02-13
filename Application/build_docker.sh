#!/bin/bash

VERSION=$1

docker build --tag moonid:$VERSION .
docker images
