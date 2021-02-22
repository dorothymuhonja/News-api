import unittest
from app.models import News_source

class NewSourceTest(unittest.TestCase):
    def setUp(self):
        self.new_news_source = News_source('Dor-news', 'DOR News', 'Dor news for Moringa School', 'general', 'https://dorothy.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source, News_source))
        
if __name__ == '__main__':
    unittest.main()