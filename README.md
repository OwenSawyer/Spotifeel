# Spotifeel
Sentiment analysis through song valence + lyrics

# TODO
## Setup
- Upgrade webpack-dev-server (+ webpack) to 4.x compatibility
    - https://www.npmjs.com/advisories/725

## CD
- [x] dockerize before heroku (really, just run deploys fully through docker)

## BE

### API
- setup Cassandra (tables, models, saving spotify data)
- setup user endpoints (TODO - swagger setup)
- swap base python to anaconda env
- add toolkits (keras, nltk, ..)
- investigate parallel requests (asyncio / tornado)

### Data aggregation

#### Sentiment model
- H-S diagonal (pleasantness (valence) vs arousal (energy))

#### SpotifyAPI
- Dataset collection (base dataset?) + (grab recents for user)
- Dimensionality Reduction using PCA
- Anomaly detection / pruning?

#### Lyrics
- Lyric scrape (genius api) (RUN ASNYC)
- keyword extraction + cleanup (contractions etc..)

## Frontend
- some fancypants ui idk

## Extras (Post Release)
- Use Celery -> automated fetch for registered accounts
- Listen (tone/key, bpm) + week reports

# Installation

## Requirements
- python 3.x

## Running dev
* `yarn install`
* `pip3 install -r requirements.txt`
* `npm run start`
* `python manage.py sync_cassandra`
* `python manage.py seed # TODO? seed from pickles.`
* `python manage.py runserver`
* Connect to `localhost:8000`

## Cassandra
- ./manage.py sync_cassandra

## Docker
- turn off all running Docker containers
  - `docker-compose down`
- delete any persistent data
  - `rm -rf data/`
- rebuild the images
  - `docker-compose build`
  
- start Cassandra
  - `docker-compose up cassandra`

- view cluster status
  - `docker-compose run nodetool status`

- create schema
  - `docker-compose run cqlsh -f /schema.cql`

- confirm schema
  - `docker-compose run cqlsh -e "DESCRIBE SCHEMA;"`

docker ps
docker system prune
docker exec -it 426c3e50d2b0 ip addr
