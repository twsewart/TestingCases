from django.test import TestCase
from django.test import Client
import unittest
import Account
import models
from login import Login


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Account.Account.__init__(self.user1,username="user1",password="password1")

    def test_valid_login(self):
        self.setUp()
        response = self.client.post('/',{'username':'user1','password':'password1'})
        self.assertEqual(response.url,'/Home/',msg="Valid login did not succeed")


    def test_invalid_login(self):
        self.setUp()
        response = self.client.post('/',{'username':'user1','password':'!passww3@ord1'})
        self.assertEqual(response.context['message'], 'bad password',msg="Invalid login incorrectly works")

