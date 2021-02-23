import os

class Config:
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey=1d236ddbaf1a4d11a4ff7ca2a09880bc'

  
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
    
}