from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class User(DjangoCassandraModel):
    __table_name__ = 'user'

    id = columns.UUID(primary_key=True)
    display_name = columns.Text()
    uri = columns.Text()
    created = columns.DateTime()

#   For both Song/Features we are storing them akin to a timeline,
#   so for each user we want to store data sequential by time, allowing duplicate songs.
class Song(DjangoCassandraModel):
    __table_name__ = 'songs_by_user'

    class Meta:
        get_pk_field = 'uid'

    uid = columns.UUID(primary_key=True)
    created = columns.DateTime(primary_key=True, clustering_order="DESC")
    uri = columns.Text(primary_key=True)

    title = columns.Text()
    artists = columns.List(columns.Text())
    duration = columns.Double()
    album = columns.Text()
    isrc = columns.Text()

#   Should consider compressing this into the song table since it has the same per-user use case.
#   However, This might be useful in the case of when we don't care about the songs themselves, and are only running
#   an analysis of the listening styles of the user.
class Features(DjangoCassandraModel):
    __table_name__ = 'features_by_user'

    class Meta:
        get_pk_field = 'uid'

    uid = columns.UUID(primary_key=True)
    created = columns.DateTime(primary_key=True, clustering_order="DESC")
    uri = columns.Text(primary_key=True)

    key = columns.Double()
    mode = columns.Double()
    tempo = columns.Double()
    danceability = columns.Double()
    energy = columns.Double()
    loudness = columns.Double()
    speechiness = columns.Double()
    acousticness = columns.Double()
    instrumentalness = columns.Double()
    liveness = columns.Double()
    valence = columns.Double()


