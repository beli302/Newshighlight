class Source:
    '''
    News Source class to define News Source Objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

class NewsArticle:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,author,url,urlToImage,publishedAt,content):
        self.id =id
        self.title = title
        self.description = description
        self.author = author
        self.url= url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content