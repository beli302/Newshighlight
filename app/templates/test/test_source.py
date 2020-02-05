from app.models import Source

class TestSource(unittest.TestCase):
   '''
   Test case to test the behavior of the NewsSource class
   '''
   def setUp(self):
       '''
       Setup function that will run before every test
       '''
       self.new_source = Source('id','name','description','url','category','country')
   def test_instance(self):
       self.assertTrue(isinstance(self.new_source,Sources))
   def test_to_check_instance_variables(self):
       '''
       Test function to check instance variables
       '''
       self.assertEquals(self.new_source.id,'id')
       self.assertEquals(self.new_source.name,'name')
       self.assertEquals(self.new_source.description,'description')
       self.assertEquals(self.new_source.url,'url')
       self.assertEquals(self.new_source.category,'category')
       self.assertEquals(self.new_source.country,'country')


if __name__ == '__main__':
    unittest.main()