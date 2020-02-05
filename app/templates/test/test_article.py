import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles(1,'author','title','description','url','urlToImage','publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'author')
        self.assertEquals(self.new_article.title,'title')
        self.assertEquals(self.new_article.description,'description')
        self.assertEquals(self.new_article.url,'url')
        self.assertEquals(self.new_article.urlToImage,'urlToImage')
        self.assertEquals(self.new_article.publishedAt,'publishedAt')
