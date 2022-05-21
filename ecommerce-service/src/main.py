from src.frameworks.db.sqlalchemy import SQLAlchemyClient
from src.frameworks.http.flask import create_flask_app


from src.stores.http.stores_blueprint import create_stores_blueprint
from src.stores.repositories.sqlalchemy_stores_repository import SQLAlchemyStoresRepository
from src.stores.usecases.manage_stores_usecase import ManageStoresUsecase

from src.users.http.users_blueprint import create_users_blueprint
from src.users.repositories.sqlalchemy_users_repository import SQLAlchemyUsersRepository
from src.users.usecases.manage_users_usecase import ManageUsersUsecase

from src.products.http.products_blueprint import create_products_blueprint
from src.products.repositories.sqlalchemy_products_repository import SQLAlchemyProductsRepository
from src.products.usecases.manage_products_usecase import ManageProductsUsecase

from src.roles.http.roles_blueprint import create_roles_blueprint
from src.roles.repositories.sqlalchemy_roles_repository import SQLAlchemyRolesRepository
from src.roles.usecases.manage_roles_usecase import ManageRolesUsecase

# Instanciar dependencias.

sqlalchemy_client = SQLAlchemyClient()

# Stores
sqlalchemy_stores_repository = SQLAlchemyStoresRepository(sqlalchemy_client)
sqlalchemy_client.create_tables()
manage_stores_usecase = ManageStoresUsecase(sqlalchemy_stores_repository)

# Users
sqlalchemy_users_repository = SQLAlchemyUsersRepository(sqlalchemy_client)
sqlalchemy_client.create_tables()
manage_users_usecase = ManageUsersUsecase(sqlalchemy_users_repository)

# Products
sqlalchemy_products_repository = SQLAlchemyProductsRepository(sqlalchemy_client)
sqlalchemy_client.create_tables()
manage_products_usecase = ManageProductsUsecase(sqlalchemy_products_repository)

# Roles

sqlalchemy_roles_repository = SQLAlchemyRolesRepository(sqlalchemy_client)
sqlalchemy_client.create_tables()
manage_roles_usecase = ManageRolesUsecase(sqlalchemy_roles_repository)

blueprints = [    
    create_stores_blueprint(manage_stores_usecase),
    create_users_blueprint(manage_users_usecase),    
    create_products_blueprint(manage_products_usecase),    
    create_roles_blueprint(manage_roles_usecase),    
]

# Crear aplicación HTTP con dependencias inyectadas.

app = create_flask_app(blueprints)