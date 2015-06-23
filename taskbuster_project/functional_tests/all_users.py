# -*- coding: utf-8 -*-  this tells the coding of the file
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):  # create a testcase called newvtest

    def setUp(self):  # this initializes the test, opening firefox.
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  # this runs after each test and closes the browser
        self.browser.quit()

    def test_it_worked(self):  # method STARTS WITH TEST
                               # the method opens the browser and asserts that
                               # welcome to django is in the title
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django d00d', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
