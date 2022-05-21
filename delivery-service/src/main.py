from src.frameworks.db.firestore import create_firestore_client
from src.frameworks.db.redis import create_redis_client
from src.frameworks.db.sqlalchemy import SQLAlchemyClient
from src.frameworks.http.flask import create_flask_app

blueprints = []

# Crear aplicación HTTP con dependencias inyectadas.

app = create_flask_app(blueprints)