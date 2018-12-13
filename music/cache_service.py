from cassandra.cluster import Cluster
from cassandra.concurrent import execute_concurrent


class CacheService:

    def __init__(self):
        pass
        #self.cluster = Cluster(['192.168.1.1', '192.168.1.2'])
        #self.session = self.cluster.connect()

    def handle_error(self, error):
        pass

    def process_result(self, error):
        pass


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

    def get_audio_analysis(self, ids):
        return self.execute_conccurent_select('song.analysis', ids)

    def get_audio_features(self, ids):
        return self.execute_conccurent_select('song.features', ids)
