from src.frameworks.db.sqlalchemy import SQLAlchemyClient
from src.frameworks.http.flask import create_flask_app

blueprints = []

# Crear aplicación HTTP con dependencias inyectadas.

app = create_flask_app(blueprints)