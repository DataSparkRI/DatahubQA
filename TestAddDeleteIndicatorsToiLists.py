from rihub_utility import login, sign_out, create_iList
try: 
	import settings as S
except:
	ImportError
	sys.stderr.write("Error: Cannot find the 'settings.py' file")

from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

import unittest


class AddDeleteIndicators(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(1)
		self.driver.get(S.HOME_PAGE)

	def tearDown(self):
		self.driver.quit()

	def _create_iList(self):
		login(self.driver)
		self.driver.get(S.USER_PORTFOLIO_URL )

		new_ilist_btn = self.driver.find_element_by_id("new_ilist_button")
		new_ilist_btn.click()

		ilist_test_txt = "Test"
		iList_name_input = self.driver.find_element_by_id("id_ilist_name")
		iList_name_input.send_keys(ilist_test_txt)

		create_btn = self.driver.find_element_by_css_selector("#new_ilist .button")
		create_btn.click()
		self.driver.refresh()

	def test_add_indicator_to_iList(self):
		#self._create_iList()

		login(self.driver)
		create_iList(self.driver)
		self.driver.refresh()

		'''since we know the filter works from TestDataCatalogSearch, 
		   we don't need to search filters again here. This will avoid 
		   having to use WebDriverWait() which can sometimes cause
		   conflict with jax requests.
		'''
		self.driver.get(S.CATALOG_FILTER_URL)

		indicator_from_search_elem = self.driver.find_element_by_css_selector('.odd a')
		indicator_from_search = indicator_from_search_elem.text
		
		indicator_from_search_ckbx = self.driver.find_element_by_css_selector('.odd input')
		indicator_from_search_ckbx.click()

		add_btn = self.driver.find_element_by_id('indicator_list_actions_add_to_ilist')
		add_btn.click()

		self.driver.get(S.USER_PORTFOLIO_URL)
		self.driver.refresh()

		iList_to_edit = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_css_selector('.edit_ilist')))
		iList_to_edit.click()

		indicator_in_iList_elem = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_id('indicator_2362')))
		indicator_in_iList =  indicator_in_iList_elem.text
		
		self.assertEqual(indicator_from_search, indicator_in_iList)
		sign_out(self.driver)
		print 'test_add_indicator_to_iList'

	def test_delete_indicator_from_iList(self):
		login(self.driver)
		self.driver.get(S.USER_PORTFOLIO_URL)
		
		iList_to_edit = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_css_selector('.edit_ilist')))
		iList_to_edit.click()

		indicator_ckbx = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_name("indicator_id")))
		indicator_ckbx.click()

		remove_selected_btn = self.driver.find_element_by_id("indicator_list_lightbox_remove_selected")
		remove_selected_btn.click()

		exit_lightbox_btn = self.driver.find_element_by_id("cboxClose")
		exit_lightbox_btn.click()

		self.driver.refresh()

		iList_to_edit = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_css_selector('.edit_ilist')))
		iList_to_edit.click()

		empty_table_elem = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_class_name("dataTables_empty")))
		empty_table_txt = empty_table_elem.text

		self.assertEqual(empty_table_txt, 'No data available in table')
		sign_out(self.driver)

		print 'test_delete_indicator_from_iList'


if __name__ == '__main__':
    unittest.main()
