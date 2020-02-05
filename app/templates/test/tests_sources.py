from app.models import Sources

class TestSources(unittest.TestCase):
   '''
   Test case to test the behavior of the NewsSource class
   '''
   def setUp(self):
       '''
       Setup function that will run before every test
       '''
       self.new_source = Sources('','','','','','')
   def test_instance(self):
       self.assertTrue(isinstance(self.new_source,Sources))
   def test_to_check_instance_variables(self):
       '''
       Test function to check instance variables
       '''
       self.assertEquals(self.new_source.id,'')
       self.assertEquals(self.new_source.name,'')
       self.assertEquals(self.new_source.description,'')
       self.assertEquals(self.new_source.url,'')
       self.assertEquals(self.new_source.category,'')
       self.assertEquals(self.new_source.country,'')


if __name__ == '__main__':
    unittest.main()