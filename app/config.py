class Config:
    '''
    General configuration parent class
    '''
    pass

    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}f223d889bf8b45cfa72e7857b37fccce'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True