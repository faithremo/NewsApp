NEWS_API_KEY='deaf8ab923104a8dbcecd36143d0a2cf'

class Config(object):
    SECRET_KEY = 'guess-me'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    
class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False
    
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True