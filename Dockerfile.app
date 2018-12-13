FROM alpine:3.8
LABEL "version"="0.0.1"
## Default to UTF-8 file.encoding
#ENV LANG C.UTF-8
#
##----JAVA-----
#
## add a simple script that can auto-detect the appropriate JAVA_HOME value
## based on whether the JDK or only the JRE is installed
#RUN { \
#		echo '#!/bin/sh'; \
#		echo 'set -e'; \
#		echo; \
#		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
#	} > /usr/local/bin/docker-java-home \
#	&& chmod +x /usr/local/bin/docker-java-home
#ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
#ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
#
#ENV JAVA_VERSION 8u171
#ENV JAVA_ALPINE_VERSION 8.171.11-r0
#
#RUN set -x \
#	&& apk add --no-cache \
#		openjdk8="$JAVA_ALPINE_VERSION" \
#	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

RUN mkdir -p /opt
COPY ./ /opt

#----PYTHON-----

RUN apk add python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#-----NODE-----

ENV NODEJS_VERSION=8.11.3 \
    PATH=$PATH:/opt/node/bin

WORKDIR "/opt/node"

RUN apk update && apk add nodejs~=8.11.3 nodejs-npm~=8.11.3

RUN npm install -g -s --no-progress yarn && yarn

#-----CUSTOM-----
WORKDIR "/opt"
ENV PYTHONPATH /opt
## BE build
RUN mkdir -p /tmp
#RUN apk add --update python3 py3-pip bash
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -q -r /tmp/requirements.txt

RUN mkdir -p /opt && mkdir -p /opt/django


    #&& \ yarn run prune
    #&& \ yarn cache clean


RUN yarn run build
#RUN python manage.py collectstatic --noinput

##RUN adduser -D myuser
##USER myuser
#
## Run the app.  CMD is required to run on Heroku
## Expose is NOT supported by Heroku
## $PORT is set by Heroku
CMD ["sh","-c","gunicorn django.wsgi:application -w 3"]
