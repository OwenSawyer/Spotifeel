import pickle

import spotipy

from music.cache_service import CacheService


class SpotifyService:

    token_map = {}
    featureNames = ["danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness",
                    "instrumentalness", "liveness", "valence", "tempo"]

    def __init__(self, token):
        self.sp = spotipy.Spotify(auth=token)
        self.cache_service = CacheService()

    def convert_song_to_dataframe(self, song):
        pass

    def get_recent(self):
        #data = self.sp.current_user_recently_played(limit=50)
        with open('./music/samples/get_recent.pkl', 'rb') as handle:
            data = pickle.load(handle)

        results = []
        for i in data['items']:
            track = i['track']
            # title = track['name']
            # artist = track['artists'][0]['name']
            # album = track['album']['name']
            # played_at = i['played_at']

            for i in range(0, track):
                analyzed = self.sp.audio_features(track) # TODO -> cache these, search cache first.
                features = []
                for z in range(0, 11):
                    features.append(analyzed[0][self.featureNames[z]])

            results.append(features)

        return results

    def get_user_profile(self):

        try:
            #data = self.sp.current_user_playing_track()
            with open('./music/samples/get_user_profile.pkl', 'rb') as handle:
                data = pickle.load(handle)

            item = data['item']
            title = item['name']
            artist = item['artists'][0]['name']
            album = item['album']['name']
            return {'title': title, 'artist': artist, 'album': album}
        except:
            return None

    def get_audio_analysis(self, track_id):
        result = self.cache_service.get_audio_analysis([track_id])
        if not result[0]:
            #result = self.sp.audio_analysis(track_id)

            with open('./music/samples/get_audio_analysis.pkl', 'rb') as handle:
                result = pickle.load(handle)

        return result

    def get_audio_features_multi(self, tracks:list):
        results = self.cache_service.get_audio_features(tracks)
        pruned_tracks = [tracks[i] for i in range(len(tracks)) if results[i] is None]
        #api_results = self.sp.audio_features(pruned_tracks)

        with open('./music/samples/get_audio_features_multi.pkl', 'rb') as handle:
            api_results = pickle.load(handle)

        counter = 0
        for i in range(len(results)):
            if results[i] is None:
                results[i] = api_results[counter]
                counter += 1

        return results
