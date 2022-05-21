from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP

from src.stores.entities.store import Store

class SQLAlchemyStoresRepository():

    def __init__(self, sqlalchemy_client, test = False):

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "Store"

        if test:
            table_name += "_test"

        self.stores_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("name", String(50)),
            Column("description", String(50)),
            Column("address", String(50)),
            Column("store", String(50)),
            Column("created_at", TIMESTAMP),
            Column("updated_at", TIMESTAMP),
            Column("deleted_at", TIMESTAMP, nullable = True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Store, self.stores_table)

    def get_stores(self):
        
        with self.session_factory() as session:
            
            stores = session.query(Store).filter_by(deleted_at = None).all()
            return stores

    def get_store(self, id):
        
        with self.session_factory() as session:

            store = session.query(Store).filter_by(id = id, deleted_at = None).first()
            return store

    def create_store(self, store):

        with self.session_factory() as session:

            session.add(store)
            session.commit()

            return store

    def update_store(self, id, fields):
        
        with self.session_factory() as session:

            session.query(Store).filter_by(id = id, deleted_at = None).update(fields)
            session.commit()
            
            store = session.query(Store).filter_by(id = id, deleted_at = None).first()
            return store

    def hard_delete_store(self, id):

        with self.session_factory() as session:

            store = session.query(Store).get(id)
            session.delete(store)
            session.commit()

    def hard_delete_all_stores(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(Store).delete()
                session.commit()

    def drop_stores_table(self):

        if self.test:
            self.client.drop_table(self.stores_table)