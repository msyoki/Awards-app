from django.test import TestCase
from .models import Profile,Project
# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        '''
        run before test
        '''
        self.profile1=Profile(name='Musyoki',bio='Software developer at Moringa School',email='msyokimutua@gmail.com')

    def test_instance(self):
        '''
        test object initialization
        '''
        self.assertTrue(isinstance(self.profile1,Profile))


    