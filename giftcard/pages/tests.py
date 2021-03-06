from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from .views import LandingPageView 


class HomepageTests(SimpleTestCase):

   def setUp(self):
      url = reverse('home')
      self.response = self.client.get(url)

   def test_homepage_status_code(self):
      self.assertEqual(self.response.status_code, 200)

   def test_homepage_template(self):
      self.assertTemplateUsed(self.response, 'index.html')

   def test_homepage_contains_correct_html(self):
      self.assertContains(self.response, 'Giftcard')

   def test_homepage_does_not_contain_incorrect_html(self):
      self.assertNotContains(
      self.response, 'Error 404')

   def test_homepage_url_resolves_homepageview(self): 
      view = resolve('/')
      self.assertEqual(
      view.func.__name__, LandingPageView.as_view().__name__
   )