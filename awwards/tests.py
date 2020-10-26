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
        test profile object initialization
        '''
        self.assertTrue(isinstance(self.profile1,Profile))


    def test_save(self):
        '''
        test profile save method
        '''
        self.profile1.save()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>=1)


class ProjectTest(TestCase):
    def setUp(self):
        '''
        run before test
        '''
        self.project1=Project(name='project1',description='This is a description of a test project',link='www.testproject.com')

    def test_instance(self):
        '''
        test project object initialization
        '''
        self.assertTrue(isinstance(self.project1,Project))


    def test_save(self):
        '''
        test profile save method
        '''
        self.project1.save()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>=1)