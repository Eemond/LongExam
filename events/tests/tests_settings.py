from django.test import SimpleTestCase
from django.conf import settings
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

class SettingsTest(SimpleTestCase):
    def test_debug_mode(self):
        self.assertTrue(settings.DEBUG)

    def test_base_dir_exists(self):
        self.assertTrue(BASE_DIR.exists())

    def test_static_url(self):
        self.assertEqual(settings.STATIC_URL, '/static/')

    def test_staticfiles_dirs(self):
        self.assertIn(os.path.join(BASE_DIR, 'static'), settings.STATICFILES_DIRS)

    def test_database_engine(self):
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.mysql')

    def test_database_name(self):
        self.assertEqual(settings.DATABASES['default']['NAME'], 'sem4pre')

    def test_database_user(self):
        self.assertEqual(settings.DATABASES['default']['USER'], 'root')

    def test_database_password(self):
        self.assertEqual(settings.DATABASES['default']['PASSWORD'], '')

    def test_database_host(self):
        self.assertEqual(settings.DATABASES['default']['HOST'], 'localhost')

    def test_database_port(self):
        self.assertEqual(settings.DATABASES['default']['PORT'], '3306')

    def test_database_options(self):
        self.assertEqual(settings.DATABASES['default']['OPTIONS']['init_command'], "SET sql_mode='STRICT_TRANS_TABLES'")
