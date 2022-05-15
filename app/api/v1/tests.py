from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from .factories import UserFactory, AdminUserFactory
from currency.models import ContactUs


class TestContactUsApiViewSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.admin = AdminUserFactory()

        cls.contact = ContactUs.objects.create(
            name="test",
            reply_to="test@gmail.com",
            subject="test1",
            body="test",
            raw_content='test text',
        )

        cls.user_client = APIClient()
        cls.admin_client = APIClient()
        cls.user_client.force_authenticate(user=cls.user)
        cls.admin_client.force_authenticate(user=cls.admin)

        cls.data = {
            'name': 'test',
            'reply_to': 'test2@gmail.com',
            'subject': 'op',
            'body': 'text',
            'raw_content': 'text',
        }
        cls.url = reverse('api:contactus-list')
        cls.detail_url = reverse('api:contactus-detail', (cls.contact.id,))

    def test_user_can_access_contact_us_list(self):
        response = self.user_client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_admin_can_access_contact_list(self):
        response = self.admin_client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_access_contact_detail(self):
        response = self.user_client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_admin_can_access_contact_detail(self):
        response = self.admin_client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_access_create_contact(self):
        response = self.user_client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_user_not_enter_data_to_create_contact(self):
        response = self.user_client.post(self.url, data={})
        self.assertEqual(response.status_code, 400)

    def test_admin_can_access_create_contact(self):
        response = self.admin_client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_user_can_access_update_contact(self):
        response = self.user_client.put(self.detail_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_admin_can_access_update_contact(self):
        response = self.admin_client.put(self.detail_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_user_can_access_delete_contact(self):
        response = self.user_client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)

    def test_admin_can_access_delete_contact(self):
        response = self.user_client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
