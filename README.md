# Spotifeel
Sentiment analysis through song valence + lyrics

# TODO
## Setup

### CD
- [x] dockerize before heroku (really, just run deploys fully through docker)

### FE
- swap React with Vue + (chartJS, vuex, hotloader) (ES2018?)
- remove project specific Django code

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
- keyword extraction + cleanup (contractions?..)

### REST Service
- Redis setup (caching?)
- User endpoints

### Frontend
- UI (does anything more need to be said?)


## Extras (Post Release)
- Listen (tone/key, bpm) + week reports

# Installing (OUTDATED)

This project requires python 3+

* `yarn install`
* `pip3 install -r requirements.txt`
* `npm run webpack`
* `python manage.py collectstatic`
* `python manage.py runserver`

## Running
* `npm run build`
- Connect to `localhost:8000

## Deploying with Docker/Heroku
heroku container:login
heroku container:push web
heroku container:release web
heroku open