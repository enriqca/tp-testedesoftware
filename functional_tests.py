import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()

class AcessLoginTest(unittest.TestCase):

  def setUp(self):
    # creating temporary directory
    try:
      os.mkdir('temp')
    except FileExistsError:
      pass

    # creating directory to Append Driver
    try:
      os.mkdir('temp/driver')
    except FileExistsError:
      pass

    # initialize the browser
    self.driver = webdriver.Chrome(ChromeDriverManager(path='temp/driver').install(),options=options)

  def tearDown(self):
    self.driver.quit()

  def test_start_web(self):
    url: str = 'http://127.0.0.1:8000/'
    self.driver.get(url=url)

    time.sleep(1)
    self.assertIn('Inicio', self.driver.title)

    self.driver.find_element(By.ID, 'login-button').send_keys(Keys.ENTER)
    self.assertIn('Login', self.driver.title)

class AcessRegisterTest(unittest.TestCase):

  def setUp(self):
    # creating temporary directory
    try:
      os.mkdir('temp')
    except FileExistsError:
      pass

    # creating directory to Append Driver
    try:
      os.mkdir('temp/driver')
    except FileExistsError:
      pass

    # initialize the browser
    self.driver = webdriver.Chrome(ChromeDriverManager(path='temp/driver').install(),options=options)

  def tearDown(self):
    self.driver.quit()

  def test_start_web(self):
    url: str = 'http://127.0.0.1:8000/'
    self.driver.get(url=url)

    time.sleep(1)
    self.assertIn('Inicio', self.driver.title)

    self.driver.find_element(By.ID, 'register-button').send_keys(Keys.ENTER)
    self.assertIn('Register', self.driver.title)