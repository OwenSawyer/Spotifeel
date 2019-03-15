#!/bin/bash

cd /var/lib/
tar xzf after_seeding.tgz
chmod -R u+rwx cassandra/data/spotifeel

cd ~/bootstrap/apache-cassandra-2.0.9
TABLE_LIST=`./bin/nodetool cfstats spotifeel | grep "Table: " | sed -e 's+^.*: ++'`
for TABLE in $TABLE_LIST; do
    echo "Restore table ${TABLE}"
    cd /var/lib/cassandra/data/spotifeel/${TABLE}
    if [ -d "snapshots/after_seeding" ]; then
        cp snapshots/after_seeding/* .
        cd ~/bootstrap/apache-cassandra-2.0.9
        ./bin/nodetool refresh -- spotifeel ${TABLE}
        cd /var/lib/cassandra/data/spotifeel/${TABLE}
        rm -rf snapshots/after_seeding
        echo "    Table ${TABLE} restored."
    else
        echo "    >>> Nothing to restore."
    fi
done