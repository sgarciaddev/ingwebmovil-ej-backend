class SQLAlchemyConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../../database/flask.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'secreto'
