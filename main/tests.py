from django.test import TestCase

class HomePageTest(TestCase):

  def test_template_inicial(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'index.html')
