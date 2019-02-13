#!/bin/bash
VERSION=$1
docker run --name moonid -d -p 8000:8000 -p 2222:2222 moonid:$VERSION
