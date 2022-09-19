from urllib import response
from django.test import TestCase
from licence.models import Licence
from django.contrib.auth.models import User
from datetime import date

# Create your tests here.
class LicenceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test', email='tom@test.com', is_superuser = True)
        self.user = User.objects.create_user(username='user2', password='test', email='user2@test.com', is_superuser = False)
        Licence.objects.create(purchase_date=date.today(), licence_type_id=1)

    def test1_logged_in_user_for_upload(self):
        login = self.client.login(username='test', password='test')
        response = self.client.get('/upload/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'licence/upload_licence.html')

    def test2_logged_in_user_update(self):
        login = self.client.login(username='test', password='test')
        licence = Licence.objects.first()
        response = self.client.get(f'/update/{licence.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'licence/upload_licence.html')

    def test3_logged_in_user_delete(self):
        login = self.client.login(username='test', password='test')
        licence = Licence.objects.first()
        response = self.client.post(f'/delete/{licence.id}')
        with self.assertRaises(Licence.DoesNotExist):
            Licence.objects.get(id=1)

    def test4_created_by_is_logged_in_user(self):
        login = self.client.login(username='test', password='test')
        data = {
            'licence_type': 1,
            'assigned_to': 7,
            'status': 1,
            'request_number': 'test',
            'cost': 10,
            'available_for_reallocation': False,
            'comment': 'test',
            'purchase_date': date.today()
        }
        response = self.client.post('/upload/', data)
        licence = Licence.objects.last()
        self.assertEqual('tom@test.com', licence.created_by)

    def test5_last_updated_by_is_logged_in_user(self):
        # First create a licence with 1 account
        login = self.client.login(username='test', password='test')
        data = {
            'licence_type': 1,
            'assigned_to': 9,
            'status': 1,
            'request_number': 'lastupdatetest',
            'cost': 10,
            'available_for_reallocation': False,
            'comment': 'test',
            'purchase_date': date.today()
        }
        response = self.client.post('/upload/', data)
        logout = self.client.logout()
        # Now update the same licence with a different account
        
        login = self.client.login(username='user2', password='test')       
        data = {
            'licence_type': 1,
            'assigned_to': 10,
            'status': 1,
            'request_number': 'test',
            'cost': 10,
            'available_for_reallocation': True,
            'comment': 'test',
            'purchase_date': date.today()
        }
        licenceId = Licence.objects.last().id
        response2 = self.client.post(f'/update/{licenceId}', data)
        licence = Licence.objects.last()
        self.assertEqual('user2@test.com', licence.last_updated_by)

    def test6_non_superuser_attempts_delete(self):
        data = {
            'licence_type': 1,
            'assigned_to': 11,
            'status': 1,
            'request_number': 'lastupdatetest',
            'cost': 10,
            'available_for_reallocation': False,
            'comment': 'test',
            'purchase_date': date.today()
        }
        response = self.client.post('/upload/', data)
        licenceId = Licence.objects.last().id
        login = self.client.login(username='user2', password='test')
        response = self.client.post(f'/delete/{licenceId}')
        self.assertTrue(Licence.objects.filter(id=licenceId).exists())

    def test7_is_superuser(self):
        login = self.client.login(username='test', password='test')
        response = self.client.get('')
        self.assertContains(response, 'Delete')

    def test8_is_not_superuser(self):
        login = self.client.login(username='user2', password='test')
        response = self.client.get('')
        self.assertNotContains(response, 'Delete')

