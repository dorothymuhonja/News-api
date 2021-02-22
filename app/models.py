class News_source:
    def __init__(self,id, name, description, category, url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url
    
    
class News_article:
    def __init__(self,source_name,author, title, description, url_link, url_image, date_published,content):
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.url_link = url_link
        self.url_image = url_image
        self.date_published = date_published
        self.content = content