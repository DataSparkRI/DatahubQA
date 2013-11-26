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



class DataCatalogTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(1)
		self.browser.get(S.INDICATOR_SEARCH_URL)

	def tearDown(self):
		self.browser.quit()

	#Filters with guaranteed results
	def _input_filters(self):
		terms_field = self.browser.find_element_by_id("indicator_field_text_search")
		terms_field.send_keys("health")

		data_level_ckbx = self.browser.find_element_by_id("id_data_levels_0")
		data_level_ckbx.click()

		data_source_ckbx = self.browser.find_element_by_id("id_data_sources_1")
		data_source_ckbx.click()
	

	#if no filters are selected there should be 0 results
	def test_results_without_filter(self):
		go_btn = self.browser.find_element_by_css_selector("#indicator_search_filter .button")
		go_btn.click();

		results_div = self.browser.find_element_by_id("indicator_search_tallies_totals")
		regex = re.compile("\d+")
		results, cross_agency = regex.findall(results_div.text)

		results = int(results)
		cross_agency = int(results)

		self.assertEqual(0, results)

	#if filters are selected there should be more than 0 results for searches that contain data	
	#this test submits filters with guaranteed results
	def test_results_with_filter(self):
		self._input_filters()

		go_btn = self.browser.find_element_by_css_selector("#indicator_search_filter .button")
		go_btn.click();

		results_div = self.browser.find_element_by_id("indicator_search_tallies_totals")
		regex = re.compile("\d+")
		results, cross_agency = regex.findall(results_div.text)

		results = int(results)
		cross_agency = int(results)

		self.assertTrue(results>0)

	#if user chooses to clear results then there should be none in the grid
	def test_clear_search(self):
		self._input_filters()

		clear_btn = self.browser.find_element_by_css_selector("#indicator_search_filter_buttons a")
		clear_btn.click()

		instructions = self.browser.find_element_by_css_selector(".grid_8 p")

		self.assertEqual("Use the keyword filter box to view available indicators.", instructions.text)


if __name__ == '__main__':
    unittest.main()

