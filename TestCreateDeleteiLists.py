from rihub_utility import login, sign_out, create_iList
try: 
	import settings as S
except:
	ImportError
	sys.stderr.write("Error: Cannot find the 'settings.py' file")

from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import re

class CreateDeleteiList(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(1)
		self.driver.get(S.HOME_PAGE)

	def tearDown(self):
		self.driver.quit()

	#Ensures the iLists are updated when user "adds" a new one. Sometimes Selenium performs faster than an 
	# ajax request is posted to page, if this happens this can result in a failed test. 
	def test_add_new_iList(self):
		login(self.driver)
		self.driver.get(S.USER_PORTFOLIO_URL)

		create_iList(self.driver)
		self.driver.refresh()

		self.page = self.driver.page_source
		self.assertTrue('Test-iList' in self.page)

		sign_out(self.driver)

		print '''test_adding_new_iList'''

	#b/c the existing iLists appear upon page load, there are no conflicts with selenium and ajax when testing deleting ilists
	def test_deleting_iList(self):
		login(self.driver)
		self.driver.get(S.USER_PORTFOLIO_URL)

		iList_to_delete = self.driver.find_element_by_class_name("delete_ilist")
		iList_to_delete.click()

		self.driver.refresh()

		self.page = self.driver.page_source
		self.assertTrue("Test-iList" not in self.page)

		sign_out(self.driver)

		print '''test_deleting_iList'''


if __name__ == '__main__':
    unittest.main()




