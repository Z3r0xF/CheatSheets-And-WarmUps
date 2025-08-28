#!/bin/bash

podman build -t helloworld-webapp .
podman run -d --replace --name "HelloWorldWebAppContainer" -p 8080:80 helloworld-webapp
