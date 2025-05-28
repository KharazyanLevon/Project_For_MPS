__all__ = ()

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Text
from .services import TextValidator


class TextTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.admin = User.objects.create_user(username='admin', password='12345', is_staff=True)
        self.text = Text.objects.create(title='Test Text', content='Content', author=self.user)

    def test_text_list_api(self):
        response = self.client.get(reverse('text_list_api'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Text')

    def test_delete_text_as_admin(self):
        self.client.login(username='admin', password='12345')
        response = self.client.get(reverse('delete_text', args=[self.text.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Text.objects.filter(id=self.text.id).exists())

    def test_validate_content(self):
        validator = TextValidator()
        self.assertTrue(validator.validate_content('Test content with 10 chars'))
        with self.assertRaises(ValueError):
            validator.validate_content('Short')

    def test_create_text(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_text'), {'title': 'New Text', 'content': 'New content'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Text.objects.filter(title='New Text').exists())