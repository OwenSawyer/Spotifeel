import collections
import pickle
import json

import datetime
from spotipy import util

from api.models import User
from api.music.query_manager import QueryManager
from api.music.spotify_service import SpotifyService

# Quick and dirty script to add my recent tracks to cassandra before I get the full fledged services running.
def add_recent():
    with open('C:/Users/Owen/Desktop/Projects/spotify.txt', 'r') as fp:
        env = fp.readlines()
        env = [i.strip() for i in env]

    # token = util.prompt_for_user_token(env[1], env[0], client_id=env[2],
    #                                    client_secret=env[3],
    #                                    redirect_uri='http://localhost:3000/callback')
    sp = SpotifyService(env[2], env[3],'http://localhost:3000/callback', env[0])
    #print(sp.get_recent())
    print(sp.get_user_profile())

def print_sample_data():

    with open('sample.txt', 'w+') as fp:
        with open('./api/music/samples/get_user_profile.pkl', 'rb') as handle:
            fp.write(str(pickle.load(handle)) + '\n')

        with open('./api/music/samples/get_recent.pkl', 'rb') as handle:
            api_results = pickle.load(handle)
            fp.write(str(next(track for track in api_results['items'] if track['track']['id']=='14JzyD6FlBD5z0wV5P07YI')) + '\n')

        with open('./api/music/samples/get_audio_features.pkl', 'rb') as handle:
            fp.write(str(pickle.load(handle)) + '\n')

        with open('./api/music/samples/get_audio_analysis.pkl', 'rb') as handle:
            fp.write(str(pickle.load(handle)) + '\n')


if __name__=='__main__':
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
    django.setup()
