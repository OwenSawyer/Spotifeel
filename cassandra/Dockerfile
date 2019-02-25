FROM cassandra:3.11

# install collectd
# NOTE: jessie packages are now being included since librrd4 and
# libmicrohttpd10 were missing from the stretch repos
RUN set -x \
    && echo "deb http://pkg.ci.collectd.org/deb jessie collectd-5.7" \
        > /etc/apt/sources.list.d/pkg.ci.collectd.org.list \
    && gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys 3994D24FB8543576 \
        && gpg --export -a 3994D24FB8543576 | apt-key add - \
    && apt-get update \
        && apt-get install -y --no-install-recommends \
            collectd=5.7.1-1.1 \
            collectd-utils \
            libprotobuf-c-dev \
            libmicrohttpd-dev \
    && echo "deb http://deb.debian.org/debian jessie main" \
        >> /etc/apt/sources.list.d/pkg.ci.collectd.org.list \
    && apt-get update \
        && apt-get install -y \
            librrd4 \
            libmicrohttpd10 \
        && rm -rf /var/lib/apt/lists/*
RUN touch /var/log/collectd.log \
    && chown cassandra:cassandra /var/log/collectd.log

COPY docker-entrypoint.sh /docker-entrypoint.sh

# does not work for some reason
#RUN echo "exec service collectd start &" \
#    >> /etc/cassandra/cassandra-env.sh
