from django.test import TestCase
from events.models import GeeksModel

class GeeksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        GeeksModel.objects.create(
            title='Test Title',
            description='Test Description',
            img='test_image.jpg'
        )

    def test_title_max_length(self):
        geek = GeeksModel.objects.get(id=1)
        max_length = geek._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_description_field(self):
        geek = GeeksModel.objects.get(id=1)
        field = geek._meta.get_field('description')
        self.assertEqual(field.verbose_name, 'description')
        self.assertEqual(field.blank, False)
        self.assertEqual(field.null, False)

    def test_last_modified_auto_now_add(self):
        geek = GeeksModel.objects.get(id=1)
        field = geek._meta.get_field('last_modified')
        self.assertTrue(field.auto_now_add)

    def test_img_upload_to(self):
        geek = GeeksModel.objects.get(id=1)
        field = geek._meta.get_field('img')
        self.assertEqual(field.upload_to, 'images/')

    def test_str_method(self):
        geek = GeeksModel.objects.get(id=1)
        self.assertEqual(str(geek), 'Test Title')
