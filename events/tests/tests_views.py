from django.test import SimpleTestCase
from django.urls import reverse, resolve
from events import views

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)
        
    def test_card_url_is_resolved(self):
        url = reverse('card')
        self.assertEqual(resolve(url).func, views.card)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, views.contact)
    