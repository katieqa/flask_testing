from unittest import TestCase
from app import app

#superclassed TestCase
class BaseTest(TestCase):
    def setUp(self):
        app.testing = True #Tells flask for lifetime of app we are in testing mode; surfaces errors slightly differently
        self.app = app.test_client
