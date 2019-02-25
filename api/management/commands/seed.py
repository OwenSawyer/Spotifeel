import collections

import datetime
import pickle
import uuid

from django.core.management.base import BaseCommand

from api.models import User, Song, Features
from api.music.query_manager import QueryManager
from api.music.spotify_service import SpotifyService

class Command(BaseCommand):
    help = 'insert a single row into each table for testing purposes.'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        query_manager = QueryManager()

        query_manager.batch_insert(User, self.handle_user())
        query_manager.batch_insert(Song, self.handle_songs())
        query_manager.batch_insert(Features, self.handle_features())

    def handle_user(self):
    #     id UUID,
    # uri text,
    # display_name text,
    # created timestamp,
        user_json = {'country': 'CA', 'display_name': 'owen135731', 'email': 'owen135731@yahoo.com',
                     'external_urls': {'spotify': 'https://open.spotify.com/user/owen135731'},
                     'followers': {'href': None, 'total': 1}, 'href': 'https://api.spotify.com/v1/users/owen135731',
                     'id': 'owen135731', 'images': [], 'product': 'premium', 'type': 'user',
                     'uri': 'spotify:user:owen135731'}

        formatted = {
            'id': uuid.uuid1(),
            'uri': user_json['uri'],
            'display_name': user_json['display_name'],
            'created': datetime.datetime.now()
        }
        return [formatted]

    def handle_songs(self):

        def handle_song(song_json):
            #     uid UUID,
            # uri text,
            # created timestamp,
            # title text,
            # artists = columns.List(columns.Text())
            # duration = columns.Double()
            # album text,
            # isrc text,
            formatted = {
                'uid': uuid.uuid1(),
                'uri': song_json['track']['uri'],
                'created': datetime.datetime.now(),
                'title': song_json['track']['name'],
                'artists': [artist['name'] for artist in song_json['track']['artists']],
                'duration': song_json['track']['duration_ms'],
                'album': song_json['track']['album']['name'],
                'isrc': song_json['track']['external_ids']['isrc'],
            }
            return formatted

        user_json = [{'track':
                         {'album':
                              {'album_type': 'single',
                               'id': '2DfPdWWXknoGKrfa2Eicyw',
                               'images': [
                                   {'height': 640, 'url': 'https://i.scdn.co/image/b322fdd64bf41d292684ca57a919d5fc9c537072', 'width': 640},
                                   {'height': 300, 'url': 'https://i.scdn.co/image/dac72574e36bfd450b44de0f0d8e78164f63eb4d', 'width': 300},
                                   {'height': 64, 'url': 'https://i.scdn.co/image/40aefbf33d89b6292973941739940b900a95e607', 'width': 64}
                               ],
                               'name': "when the party's over",
                               'type': 'album',
                               'uri': 'spotify:album:2DfPdWWXknoGKrfa2Eicyw'
                               },
                          'artists': [
                              {'external_urls': {
                                  'spotify': 'https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH'},
                               'href': 'https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH',
                               'id': '6qqNVTkY8uBg9cP3Jd7DAH',
                               'name': 'Billie Eilish',
                               'type': 'artist',
                               'uri': 'spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH'}
                          ],
                          'duration_ms': 199931,
                          'explicit': False,
                          'external_ids': {
                              'isrc': 'USUM71815958'},
                          'external_urls': {
                              'spotify': 'https://open.spotify.com/track/14JzyD6FlBD5z0wV5P07YI'},
                          'href': 'https://api.spotify.com/v1/tracks/14JzyD6FlBD5z0wV5P07YI',
                          'id': '14JzyD6FlBD5z0wV5P07YI',
                          'name': "when the party's over",
                          'popularity': 93,
                          'preview_url': 'https://p.scdn.co/mp3-preview/16ec3dacdae0fddfa5e1fa25e8b7e74bbfd66a0d?cid=446bd76d6fe949cf95343091d2157fbf',
                          'track_number': 1,
                          'type': 'track',
                          'uri': 'spotify:track:14JzyD6FlBD5z0wV5P07YI'
                          },
                        'played_at': '2018-11-26T22:58:32.121Z'
                     }]
        return [handle_song(i) for i in user_json]

    def handle_features(self):

        def handle_feature(feature_json):

            formatted = {
                'uid': uuid.uuid1(),
                'uri': feature_json['uri'],
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

        #     uid UUID,
        # uri text,
        # created timestamp,
        # key double,
        # mode double,
        # tempo double,
        # danceability double,
        # energy double,
        # loudness double,
        # speechiness double,
        # acousticness double,
        # instrumentalness double,
        # liveness double,
        # valence double,
        user_json = [{'danceability': 0.486, 'energy': 0.676, 'key': 4, 'loudness': -8.377, 'mode': 1,
                      'speechiness': 0.0974, 'acousticness': 0.0436, 'instrumentalness': 2.43e-05, 'liveness': 0.0812,
                      'valence': 0.293, 'tempo': 90.242, 'type': 'audio_features', 'id': '5Q4mP2MPgZelC7soOeeARX',
                      'uri': 'spotify:track:5Q4mP2MPgZelC7soOeeARX', 'track_href': 'https://api.spotify.com/v1/tracks/5Q4mP2MPgZelC7soOeeARX',
                      'analysis_url': 'https://api.spotify.com/v1/audio-analysis/5Q4mP2MPgZelC7soOeeARX', 'duration_ms': 206000, 'time_signature': 4}]
        return [handle_feature(i) for i in user_json]
