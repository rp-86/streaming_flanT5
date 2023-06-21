#!/bin/bash

BASE_DIR = "$( pwd )"
IMAGE = "flant5-server"

docker run --rm \
        -p 8080:8080 \
        "$IMAGE"