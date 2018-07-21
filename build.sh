#!/usr/bin/env bash

heroku container:login
docker-compose up
heroku container:push web
heroku container:release web
