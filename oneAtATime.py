from rihub_utility import login, sign_out
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import unittest
import re


class UserLoginTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get('http://127.0.0.1:8000/')

	def tearDown(self):
		self.driver.quit()

	def test_removing_one_indicator_from_iList(self):
		login(self.driver)
		self.driver.get('http://127.0.0.1:8000/accounts/portfolio/')
'''		
		iList_to_edit = self.driver.find_element_by_class_name("edit_ilist")
		iList_to_edit.click()


		find_indicator = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_css_selector(".indicator_item a")))
		#indicator_to_test = find_indicator.text
		#print find_indicator

		#print indicator_to_test

		#clicks the checkbox of the indicator
		selected_indicator = self.driver.find_element_by_name("indicator_id")
		selected_indicator.click()

		remove_selected_btn = self.driver.find_element_by_id("indicator_list_lightbox_remove_selected")
		remove_selected_btn.click()

		exit_lightbox_btn = self.driver.find_element_by_id("cboxClose")
		exit_lightbox_btn.click()

		iList_to_edit = self.driver.find_element_by_class_name("edit_ilist")
		iList_to_edit.click()

		self.page = self.driver.page_source
		self.assertTrue(indicator_to_test not in self.page)

		sign_out(self.driver)

'''

if __name__ == '__main__':
    unittest.main()



'''FIX THIS!

		selected_indicator = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_name("indicator_id")))
		selected_indicator.click() 

		sort_btn = self.driver.find_element_by_xpath("//th[@class='sorting_asc']")
		sort_btn.click
		sort_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_css_selector("#indicator_lightbox_table .sorting_asc")))
		sort_btn.click()

		find_sort_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_css_selector("#indicator_lightbox_table .sorting_asc")))
		find_sort_btn.click()

		#sort_desc_btn = self.driver.find_element_by_class_name("sorting_asc")
		#sort_desc_btn.click()

		sort_desc_btn = self.driver.find_element_by_css_selector("#indicator_lightbox_table .sorting_asc")
		sort_desc_btn.click()

		While dealing with Ajax and WebDriverWait it is helpful to know a bit about exactly how the internals of WebDriverWait work. 
		In simplified terms it will check the until equation, sleep, then check the equation again until the timeout is reached. 
		The default setting for polling frequency (that means how much sleep between each the until equation) is 0.5 seconds.
		
		The tricky part, however, is that WebDriverWait will check the until equation before it performs the first sleep. Thus if your 
		Ajax has a slight delay, the very first poll of WebDriverWait might resolve true before the ajax has started. In effect, 
		the the wait will not really have occurred at all because the first sleep was never reached.
		There is no workaround for this and the only way to avoid it is to change the way or which element you are waiting for.



		('http://ridatahub.org/')

		('http://ridatahub.org/accounts/portfolio/')
'''