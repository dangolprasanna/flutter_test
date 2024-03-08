#!/usr/bin/env bash

#docker login registry.gitlab.com
docker build -t registry.gitlab.com/nicolalandro/flutter_test_app .
docker push registry.gitlab.com/nicolalandro/flutter_test_app
