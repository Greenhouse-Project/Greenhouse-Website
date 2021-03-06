'''
This file contains all of the config variables for the app
'''
class Config(object):
    """
    Common configurations:
    Put any configs here that are common accross all environments
    """
    
class DevConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True # Logging SQL errors
    SQLALCHEMY_DATABASE_URI = True # Make sure you are connecting to the right address
    
class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    
app_config ={
    'development': DevConfig,
    'production': ProductionConfig
}
