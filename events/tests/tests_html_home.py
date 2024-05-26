from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_renders_correctly(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    def test_home_page_title(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn(b'<title>Home</title>', response.content)
    
    def test_static_files_are_loaded(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'href="/static/css/styles.css"')
        self.assertContains(response, 'href="/static/image/home.ico"')
        self.assertContains(response, 'src="/static/js/scripts.js"')
