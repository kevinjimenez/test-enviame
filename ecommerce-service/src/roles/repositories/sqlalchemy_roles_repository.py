from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP

from src.roles.entities.role import Role
    
# Implementación con SQL Alchemy para el repositorio de libros.

class SQLAlchemyRolesRepository():

    def __init__(self, sqlalchemy_client, test = False):

        # Mapear la tabla role de forma imperativa.
        # Si "test" es true, se le agrega un sufijo al nombre de la tabla,
        # para que las pruebas de integración no sobreescriban los datos existentes.

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "Role"

        if test:
            table_name += "_test"

        self.roles_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("name", String(50)),
            Column("description", String(50)),            
            Column("created_at", TIMESTAMP),
            Column("updated_at", TIMESTAMP),
            Column("deleted_at", TIMESTAMP, nullable = True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Role, self.roles_table)

    def get_roles(self):
        
        with self.session_factory() as session:
            
            roles = session.query(Role).filter_by(deleted_at = None).all()
            return roles

    def get_role(self, id):
        
        with self.session_factory() as session:

            role = session.query(Role).filter_by(id = id, deleted_at = None).first()
            return role

    def create_role(self, role):

        with self.session_factory() as session:

            session.add(role)
            session.commit()

            return role

    def update_role(self, id, fields):

        # Actualiza sólo los campos de la lista "fields" en el libro especificado.
        # Luego retorna el libro con los nuevos datos.
        
        with self.session_factory() as session:

            session.query(Role).filter_by(id = id, deleted_at = None).update(fields)
            session.commit()
            
            role = session.query(Role).filter_by(id = id, deleted_at = None).first()
            return role

    def hard_delete_role(self, id):

        with self.session_factory() as session:

            role = session.query(Role).get(id)
            session.delete(role)
            session.commit()

    def hard_delete_all_roles(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(Role).delete()
                session.commit()

    def drop_roles_table(self):

        if self.test:
            self.client.drop_table(self.roles_table)