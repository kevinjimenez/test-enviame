from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP

from src.users.entities.user import User

class SQLAlchemyUsersRepository():

    def __init__(self, sqlalchemy_client, test = False):

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "User"

        if test:
            table_name += "_test"

        self.users_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("name", String(50)),
            Column("email", String(50)),
            Column("shipping_addres", String(50)),
            Column("role", String(50)),
            Column("created_at", TIMESTAMP),
            Column("updated_at", TIMESTAMP),
            Column("deleted_at", TIMESTAMP, nullable = True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(User, self.users_table)

    def get_users(self):
        
        with self.session_factory() as session:
            
            users = session.query(User).filter_by(deleted_at = None).all()
            return users

    def get_user(self, id):
        
        with self.session_factory() as session:

            user = session.query(User).filter_by(id = id, deleted_at = None).first()
            return user

    def create_user(self, user):

        with self.session_factory() as session:

            session.add(user)
            session.commit()

            return user

    def update_user(self, id, fields):
        
        with self.session_factory() as session:

            session.query(User).filter_by(id = id, deleted_at = None).update(fields)
            session.commit()
            
            user = session.query(User).filter_by(id = id, deleted_at = None).first()
            return user

    def hard_delete_user(self, id):

        with self.session_factory() as session:

            user = session.query(User).get(id)
            session.delete(user)
            session.commit()

    def hard_delete_all_users(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(User).delete()
                session.commit()

    def drop_users_table(self):

        if self.test:
            self.client.drop_table(self.users_table)