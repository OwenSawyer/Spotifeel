#!/bin/bash

cd ~/bootstrap/apache-cassandra-2.0.9
./bin/nodetool clearsnapshot -t after_seeding spotifeel
./bin/nodetool snapshot -t after_seeding spotifeel

cd /var/lib/
tar czf after_seeding.tgz cassandra/data/spotifeel/*/snapshots/after_seeding