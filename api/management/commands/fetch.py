import collections

import datetime
import pickle
import uuid

from django.core.management.base import BaseCommand

from api.models import User, Song, Features
from api.music.query_manager import QueryManager
from api.music.spotify_service import SpotifyService

class Command(BaseCommand):
    help = 'Fetches recent tracks/features for the base user (me). ' \
           'This is not an extensible solution though as number of users increases, ' \
           'as if we call fetch on all at the same time will hit the rate limit for spotify / lyric apis.' \
           'This should be moved out of a cronjob command and into an actual scheduling system (Celery?). ' \
           'Ideally it would fetch hourly based on the account creation time or something similar ' \
           '(or even simpler, just keep all accounts in a queue and fetch 1 every 5-10s)'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):


        with open('/home/osawyer/website/spotify.txt', 'r') as fp:
            env = fp.readlines()
            env = [i.strip() for i in env]

        sp = SpotifyService(env[2], env[3],'http://localhost:3000/callback', env[0])
        #print(sp.get_recent())
        print(sp.get_user_profile())

        songs = sp.get_recent()
        print(songs)
        feats = sp.get_audio_features_multi([s['uri'] for s in songs])
        print(feats)

        query_manager = QueryManager()
        song_json = self.handle_songs(songs)
        played_at = {dct['uri']:dct['played'] for dct in song_json}

        query_manager.batch_insert(Song, song_json)
        query_manager.batch_insert(Features, self.handle_features(feats, played_at))

    def handle_songs(self, user_json):

        def handle_song(song_json):
            formatted = {
                'uid': uuid.uuid1(),
                'uri': song_json['uri'],
                'played': song_json['played_at'],
                'created': datetime.datetime.now(),
                'title': song_json['name'],
                'artists': [artist['name'] for artist in song_json['artists']],
                'duration': song_json['duration_ms'],
                'album': song_json['album']['name'],
                'isrc': song_json['external_ids']['isrc'],
            }
            return formatted

        return [handle_song(i) for i in user_json]

    def handle_features(self, user_json, played_at):

        def handle_feature(feature_json, played_at):

            formatted = {
                'uid': uuid.uuid1(),
                'uri': feature_json['uri'],
                'played': played_at[feature_json['uri']],
                'created': datetime.datetime.now(),
                'key': feature_json['key'],
                'mode': feature_json['mode'],
                'tempo': feature_json['tempo'],
                'danceability': feature_json['danceability'],
                'energy': feature_json['energy'],
                'loudness': feature_json['loudness'],
                'speechiness': feature_json['speechiness'],
                'acousticness': feature_json['acousticness'],
                'instrumentalness': feature_json['instrumentalness'],
                'liveness': feature_json['liveness'],
                'valence': feature_json['valence']
            }
            return formatted

        return [handle_feature(i, played_at) for i in user_json]


# if __name__=='__main__':
#     seeder = Seed()
#     seeder.print_sample_data()
