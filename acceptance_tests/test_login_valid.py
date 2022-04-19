from django.test import TestCase
from django.test import Client
from Admin import username, password
from TA import username, password
from user import username, password


class TestingD(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Admin.objects.__init__(name='username1',password='myPassword1')
        self.user2 = Admin.objects.__init__(name='username2', password='myPassword2')

    def test_Admin_valid_login(self):
        self.user1 = Admin.objects.__init__(name='username1',password='myPassword1')
        self.assertEqual(login(user1.name,user1.password) == True,msg="Correct login info did not work")

    def test_TA_valid_login(self):
        self.user1 = TA.objects.__init__(name='username1',password='myPassword1')
        self.assertEqual(login(user1.name,user1.password) == True,msg="Correct login info did not work")

    def test_USER_valid_login(self):
        self.user1 = user.objects.__init__(name='username1',password='myPassword1')
        self.assertEqual(login(user1.name,user1.password) == True,msg="Correct login info did not work")