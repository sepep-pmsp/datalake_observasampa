import pandas as pd
from sqlalchemy import create_engine

class TrinoSQLAlchemy(object):
    ''' Class for work with Trino, SQLAlchemy e Pandas '''

    def __init__(self, config):
        """ Initialising object
        Parameters
        ----------
        config : dict
            config of module
        """
        self.config = config
        self.engine = None

        self.host = 'localhost'
        if 'TRINO_HOST' in self.config:
            self.host = self.config['TRINO_HOST']
        self.port = '8888'
        if 'TRINO_PORT' in self.config:
            self.port = self.config['TRINO_PORT']
        self.url = "%s:%s" % (self.host, self.port)
        self.db = ''
        if 'TRINO_DB' in self.config:
            self.db = self.config['TRINO_DB']
        self.user = ''
        if 'TRINO_USER' in self.config:
            self.user = self.config['TRINO_USER']
        self.url = 'trino://%s/%s/' % (self.url, self.db)
        self.get_engine_trino()

    def get_engine_trino(self):
        self.engine = create_engine(self.url,
                                    connect_args={'user': self.user})
        return self.engine

    def trino_read_tables(self, src, table_name):
        if self.engine is None:
            self.get_engine_trino()
        connection = self.engine.connect()
        query = "SELECT * FROM {db}.{src}.{table_name}".format(db=self.db,
                                                               src=src,
                                                               table_name=table_name)
        return pd.read_sql(query, connection)

    def export_to_trino(self, df, table_name, dest, method, index, if_exists):
        if self.engine is None:
            self.get_engine_trino()
        return df.to_sql(name=table_name, con=self.engine,
                         schema=dest, method=method, index=index,
                         if_exists=if_exists)
