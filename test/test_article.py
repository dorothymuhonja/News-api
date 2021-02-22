import unittest
from app.models import News_article

class NewsArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_news_article = News_article('Dor','Dorothy','dor-news', 'Dorothy starts programming', 'https://dorothy.com', 'https://dorothy.dorothy/moringadaily', '2020-09-13 13:23','Coding gets complex')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article, News_article))
        
if __name__ == '__main__':
    unittest.main()