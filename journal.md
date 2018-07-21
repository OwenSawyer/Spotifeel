# July 22 2018
## Status: Basic setup (Dev complete ; Prod incomplete)
## Notes 
### Hosting
- Heroku does not integrate with docker compose; have to push each docker image separately
- Heroku charges for cassandra instances (72$/mo wtf) - exploring alternate options (AWS, DigitalOcean -> 5$/mo)
- Given the two above, most likely host the base Docker instance on Heroku and have the backend connect to externally hosted Cassandra instance.
- Alternatively, just use AWS/DigitalOcean to host it all (bonus: docker-compose suppport)
### Architecture
- Too many misc files (Procfile, \.*, build/config) - can be greatly simplified given the expected complexity of the application
- Docker builds are 500/200mb for app/cassandra respective. Not happy with the size of the app build, however not sure how much this can be reduced (give the size of npm packages)
