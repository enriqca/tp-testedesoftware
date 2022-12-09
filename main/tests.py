from django.test import TestCase

class HomePageTest(TestCase):

  def test_template_inicial(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'index.html')

  def test_template_login(self):
    response = self.client.get('/cadastro')
    self.assertTemplateUsed(response,'cadastro.html')

  def test_template_register(self):
    response = self.client.get('/login')
    self.assertTemplateUsed(response,'login.html')
