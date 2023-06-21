#!/bin/bash

BASE_DIR = "$( pwd )"
DOCKERFILE = "$BASE_DIR/Dockerfile"

DOCKER_BUILDKIT=1 docker build -t flant5-server -f "$DOCKERFILE" "$BASE_DIR"