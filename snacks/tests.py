from django.test import TestCase
from django.urls import reverse


class SnacksTests(TestCase):
  def test_home_status(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  
  def test_home_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')
  
  def test_snack_detail_status(self):
    url = reverse('snack_detail', args=[1])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  
  # def test_snack_detail_template(self):
  #   url = reverse('snack_detail',args=(1,))
  #   response = self.client.get(url)
  #   self.assertTemplateUsed(response, 'snack_detail.html')
  #   self.assertTemplateUsed(response, 'base.html')
