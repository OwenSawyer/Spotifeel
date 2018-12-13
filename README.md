# Spotifeel
Sentiment analysis through song valence + lyrics

# TODO
### Setup
- Upgrade webpack-dev-server (+ webpack) to 4.x compatibility
    - https://www.npmjs.com/advisories/725


### CD
- [x] dockerize before heroku (really, just run deploys fully through docker)

### BE
- swap base python to anaconda env
- add toolkits (keras, nltk, ..)
- investigate parallel requests (asyncio / tornado)

## Development

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

### REST Service
- Cassandra setup
- User endpoints

### Frontend
- some fancypants ui idk

## Extras (Post Release)
- Use Celery -> automated fetch for registered accounts
- Listen (tone/key, bpm) + week reports

# Installation

This project requires python 3+

## Running dev
* `yarn install`
* `pip3 install -r requirements.txt`
* `npm run start`
* `python manage.py runserver`
* Connect to `localhost:8000`

## Deploying with Docker/Heroku
- heroku container:login
- heroku container:push app cassandra --recursive
- heroku container:release app cassandra

## Cassandra
- ./manage.py sync_cassandra
