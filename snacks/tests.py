from django.test import SimpleTestCase
from django.urls import reverse

# NEEDS update
class SnacksTests(SimpleTestCase):
  def test_home_status(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  
  def test_home_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'base.html')
  
  def test_about_status(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  
  def test_about_template(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    self.assertTemplateUsed(response, 'base.html')
  
  def test_not_fount(self):
    url = 'unknown/'
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)
