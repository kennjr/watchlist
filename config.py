# The class below is the parent config class and the configurations added to this class will be used by both
# the ProdConfig and DevConfig
import os


class Config:
    """
    The general configs parent class
    """
    # API_KEY = "6be093a1a0f961d1b8df3150cdc2eae9"
    MOVIES_DB_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}"
    MOVIE_API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLAlchemy = "postgresql+psycopg2://kenny:password@localhost/watchlist"

class ProdConfig(Config):
    """
    Configurations for the app when it's in production mode
    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass


class DevConfig(Config):
    """
    Configurations for the app when it's in development phase/mode
    Args:
        Config: The parent configuration class with General configuration settings
    """
    # Setting the debug to True allows us to catch errors real quick
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
