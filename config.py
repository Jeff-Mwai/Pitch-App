import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:KingJeffa00*@localhost/watchlist'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}