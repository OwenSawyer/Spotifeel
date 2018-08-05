import spotipy


class SpotifyService:

    token_map = {}
    featureNames = ["danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness",
                    "instrumentalness", "liveness", "valence", "tempo"]

    def __init__(self, token):
        self.token = token
        self.sp = spotipy.Spotify(auth=self.token)

    def convert_song_to_dataframe(self, song):
        pass

    def get_recent(self):
        data = self.sp.current_user_recently_played(limit=25)
        results = []

        for i in data['items']:
            track = i['track']
            # title = track['name']
            # artist = track['artists'][0]['name']
            # album = track['album']['name']
            # played_at = i['played_at']

            for i in range(0, track):
                analyzed = self.sp.audio_features(track)
                features = []
                for z in range(0, 11):
                    features.append(analyzed[0][self.featureNames[z]])

            results.append(features)

        return results

    def current(self):

        try:
            data = self.sp.current_user_playing_track()
            item = data['item']
            title = item['name']
            artist = item['artists'][0]['name']
            album = item['album']['name']
            return {'title': title, 'artist': artist, 'album': album}
        except:
            return None
