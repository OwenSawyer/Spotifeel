FROM beevelop/nodejs-python:latest
LABEL "version"="0.0.1"

## BE build
RUN mkdir -p /tmp
#RUN apk add --update python3 py3-pip bash
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -q -r /tmp/requirements.txt


#WORKDIR /code
#ADD . /code
RUN mkdir -p /opt && mkdir -p /opt/drf_react
WORKDIR /opt/


#
#RUN apt-get update \
#    && apt-get upgrade -y \
#    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
#    && apt-get install -y nodejs
COPY package.json /opt/
#RUN rm -rf node_modules

RUN npm install -g -s --no-progress yarn && yarn
    #&& \ yarn run prune
    #&& \ yarn cache clean

ADD . /opt

RUN yarn run prod-postbuild
RUN python manage.py collectstatic --noinput

#/opt/node/bin/yarn -> /opt/node/lib/node_modules/yarn/bin/yarn.js
#/opt/node/bin/yarnpkg -> /opt/node/lib/node_modules/yarn/bin/yarn.js
#/opt/node/lib
#`-- yarn@1.7.0


#
##RUN adduser -D myuser
##USER myuser
#
## Run the app.  CMD is required to run on Heroku
## Expose is NOT supported by Heroku
## $PORT is set by Heroku
##CMD ["node ./opt/server.js && gunicorn drf_react.wsgi -w 3"]
#CMD ["sh","-c","node server.js"]
CMD ["sh","-c","gunicorn drf_react.wsgi -w 3"]

#CMD ["node server.js"]