from django.test import SimpleTestCase
from django.urls import reverse, resolve
from events import views
from django.contrib import admin

class TestUrls(SimpleTestCase):

    def test_admin_url_is_resolved(self):
        url = reverse('admin:index')
        view = resolve(url).func
        self.assertEqual(view.__name__, admin.site.index.__name__)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        view = resolve(url).func
        self.assertEqual(view, views.home)

    def test_card_url_is_resolved(self):
        url = reverse('card')
        view = resolve(url).func
        self.assertEqual(view, views.card)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        view = resolve(url).func
        self.assertEqual(view, views.contact)
