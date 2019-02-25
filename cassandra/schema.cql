DROP KEYSPACE IF EXISTS spotifeel;

CREATE KEYSPACE spotifeel WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE spotifeel;

CREATE TABLE user (
    id UUID,
    display_name text,
    uri text,
    created timestamp,
    PRIMARY KEY (id)
) WITH COMMENT = 'user';

CREATE TABLE songs_by_user (
    uid UUID,
    uri text,
    created timestamp,
    title text,
    artists list<text>,
    duration double,
    album text,
    isrc text,
    PRIMARY KEY(uid, created, uri)
) WITH CLUSTERING ORDER BY (created DESC)
  AND COMMENT = 'songs by user';

CREATE TABLE features_by_user (
    uid UUID,
    uri text,
    created timestamp,
    key double,
    mode double,
    tempo double,
    danceability double,
    energy double,
    loudness double,
    speechiness double,
    acousticness double,
    instrumentalness double,
    liveness double,
    valence double,
    PRIMARY KEY(uid, created, uri)
) WITH CLUSTERING ORDER BY (created DESC)
  AND COMMENT = 'features by user';
