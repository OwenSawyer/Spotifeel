import pickle

import spotipy
from spotipy import oauth2

with open('/home/osawyer/website/spotify.txt', 'r') as fp:
    env = fp.readlines()
    env = [i.strip() for i in env]



class SpotifyService:

    token_map = {}
    featureNames = ["danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness",
                    "instrumentalness", "liveness", "valence", "tempo"]

    # TODO : Need to support functionality for user context switching?
    def __init__(self, client_id, client_secret, redirect_uri, scopes):

        self.sp_oauth = oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                                       scope=scopes)

        self.sp_oauth.cache_path = '/home/osawyer/website/cache-temp' # hacky workaround while in development
        self.token_info = self.sp_oauth.get_cached_token()

        if not self.token_info:
            auth_url = self.sp_oauth.get_authorize_url(show_dialog=True)
            print(auth_url)
            response = input('Paste the above link into your browser, then paste the redirect url here: ')

            code = self.sp_oauth.parse_response_code(response)
            self.token_info = self.sp_oauth.get_access_token(code)
            token = self.token_info['access_token']

        elif self.sp_oauth.is_token_expired(self.token_info):

            self.token_info = self.sp_oauth.refresh_access_token(self.token_info['refresh_token'])
            print("Using refresh token")

        else:
            print("Using cached token")

        token = self.token_info['access_token']

        self.sp = spotipy.Spotify(auth=token)

    def convert_song_to_dataframe(self, song):
        pass

    def get_user_profile(self):

        try:
            data = self.sp.current_user()
            # with open('./api/music/samples/get_user_profile.pkl', 'wb') as handle:
            #     pickle.dump(data,handle)

            return data
        except:
            return None

    def get_recent(self):
        data = self.sp.current_user_recently_played(limit=5)

        results = []
        tracks = []
        for i in data['items']:
            #track = i['track']
            tracks.append(i['track'])

        # title = track['name']
            # artist = track['artists'][0]['name']
            # album = track['album']['name']
            # played_at = i['played_at']

            #analyzed = self.sp.audio_features(track) # TODO -> cache these, search cache first.
            #features = []
            #for z in range(0, 11):
            #    features.append(analyzed[0][self.featureNames[z]])

            #results.append(features)

        return tracks

    def get_audio_features_multi(self, tracks:list):
        #results = self.cache_service.get_audio_features(tracks)
        results = [None for _ in range(len(tracks))]
        pruned_tracks = [tracks[i] for i in range(len(tracks)) if results[i] is None]
        api_results = self.sp.audio_features(pruned_tracks)

        counter = 0
        for i in range(len(results)):
            if results[i] is None:
                results[i] = api_results[counter]
                counter += 1

        return results

    def get_audio_analysis(self, track_id):
        result = self.cache_service.get_audio_analysis([track_id])
        if not result[0]:
            result = self.sp.audio_analysis(track_id)

        return result
