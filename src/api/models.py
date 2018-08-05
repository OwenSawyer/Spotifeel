from uuid import uuid4, uuid1
#from cassandra.cqlengine import columns
#from django_cassandra_engine.models import DjangoCassandraModel

#
# class BaseModel(DjangoCassandraModel):
#     __abstract__ = True
#
#     id = columns.UUID(primary_key=True, default=uuid4)
#     creation_timestamp = columns.TimeUUID(default=uuid1)
#     deleted = columns.Boolean(default=False)


class User():
    pass
#    email = columns.Integer(index=True)
#    name = columns.Text()


class Record(): #TODO - is there a better name for this? (milestone? landmark?)
    pass
    # user_id = columns.UUID(primary_key=True, index=True) #cluster key
    # timestamp = columns.DateTime(primary_key=True, index=True, clustering_order='DESC')
    # size = columns.BigInt()
    # acousticness = columns.Double()
    # danceability = columns.Double()
    # energy = columns.Double()
    # instrumentalness = columns.Double()
    # loudness = columns.Double()
    # speechiness = columns.Double()
    # tempo = columns.Double()
    # valence = columns.Double()


