from django.test import TestCase
from django.urls import reverse

class ContactPageTest(TestCase):
    def test_contact_page_renders_correctly(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_static_files_are_loaded(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'href="/static/css/contact.css"')
        self.assertContains(response, 'href="/static/image/contact.ico"')
        self.assertContains(response, 'src="/static/js/contact.js"')
