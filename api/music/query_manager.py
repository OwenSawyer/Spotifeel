
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, ResultSet
from cassandra.concurrent import execute_concurrent
from cassandra.query import BatchStatement
from django_cassandra_engine.models import DjangoCassandraModel


class QueryManager:

    def __init__(self):
        pass
        self.cluster = Cluster(['127.0.0.1'],  port=9042)
        self.session = self.cluster.connect("spotifeel")

    def handle_error(self, error):
        print(error)

    def process_result(self, result):
        print(result)

    # TODO: restrict queries by timestamp range
    def batch_insert(self, table_model: DjangoCassandraModel, items: list):

        # query = """
        # INSERT INTO table_name (
        #     field_1,
        #     field_2
        # ) VALUES (?, ?)
        # """
        # cql_session.prepare(query).bind({'field_1': 'foo', 'field_2': 'bar'})

        def fields(self): #TODO -> make this accessible as @property of the model (ie: extend DjangoCassandraModel?)
            return [f.name for f in self._meta.fields + self._meta.many_to_many]
        #print(fields(table_model))

    # songs_by_user (created, uid) VALUES (?, ?)
    #     print(f"INSERT INTO {table_model.__table_name__} ({','.join(fields(table_model))}) "
    #           f"VALUES ({','.join(['?' for i in range(len(fields(table_model)))])})")
        insert_user = self.session.prepare(f"INSERT INTO {table_model.__table_name__} ({','.join(fields(table_model))}) "
                                           f"VALUES ({','.join(['?' for i in range(len(fields(table_model)))])})")
        batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)

        # row: (created_val, uid_val)
        for row in items:
            batch.add(insert_user.bind(row))
        response = self.session.execute(batch)
        if isinstance(response, ResultSet):
            print("success")
            #self.process_result(result[0])  # handle row
        else:
            print("fail")
            #self.handle_error(result)  # Exception, TODO
        # #print(response)
        # for (success, result) in response:
        #     print(success,result)
        #     if success:
        #         self.process_result(result[0])  # handle row
        #     else:
        #         self.handle_error(result)  # Exception, TODO

        return True

    # TODO: restrict queries by timestamp range
    def execute_conccurent_select(self, table_name, ids):
        return [None for _ in range(len(ids))]

        select_statement = self.session.prepare(f'SELECT * FROM {table_name} WHERE id=?')

        statements_and_params = []
        for id in ids:
            params = (id,)
            statements_and_params.append((select_statement, params))

        results = execute_concurrent(
            self.session, statements_and_params, raise_on_first_error=False)

        for (success, result) in results:
            if not success:
                self.handle_error(result)  # Exception, TODO
            else:
                self.process_result(result[0])  # handle row

        return results

    def get_songs(self, ids):
        return self.execute_conccurent_select('song.info', ids)

    def get_audio_features(self, ids):
        return self.execute_conccurent_select('song.features', ids)
