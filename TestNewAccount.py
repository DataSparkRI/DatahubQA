from rihub_utility import login, sign_out
try: 
	import settings as S
except:
	ImportError
	sys.stderr.write("Error: Cannot find the 'settings.py' file")

from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

import unittest


class RegistrationForm(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(10)
		self.driver.get(S.HOME_PAGE)

	def tearDown(self):
		self.driver.quit()

	def _remove_test_user_from_db(self):
		self.driver.get(S.ADMIN_LOGIN_PAGE)

		#to run this test make sure to include a superuser login name and password
		admin_username = self.driver.find_element_by_id('id_username')
		admin_username.send_keys(S.SUPERUSER_USERNAME)

		admin_password = self.driver.find_element_by_id('id_password')
		admin_password.send_keys(S.SUPERUSER_PASSWORD)
		admin_password.send_keys(Keys.RETURN)

		#this searches the test username directly into url, less complications w/selenium
		self.driver.get(S.USERNAME_SEARCH_URL)
		username_link = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_element_by_link_text('testtestspaceorg')))
		
		#ensures that this test name is actually in the db
		self.assertEqual(username_link.text,'testtestspaceorg')

		username_link.click()

		delete_btn = self.driver.find_element_by_class_name('deletelink')
		delete_btn.click()

		confirm_btn = self.driver.find_element_by_css_selector('input[type="submit"]')
		confirm_btn.click()

		logout_btn = self.driver.find_element_by_css_selector('a[href="/admin/logout/"]')
		logout_btn.click()


	def test_create_new_account(self):
		self.driver.get(S.NEW_ACCOUNT_PAGE)

		email_input = self.driver.find_element_by_id('id_email')
		email_input.send_keys('test@testspace.org')

		first_name_input = self.driver.find_element_by_id('id_first_name')
		first_name_input.send_keys('Test')

		last_name_input = self.driver.find_element_by_id('id_last_name')
		last_name_input.send_keys('McTesterson')

		password_input = self.driver.find_element_by_id('id_password1')
		password_input.send_keys('theTest11!')

		password_confrm_input = self.driver.find_element_by_id('id_password2')
		password_confrm_input.send_keys('theTest11!')

		term_of_use_ckbx = self.driver.find_element_by_id('id_tos')
		term_of_use_ckbx.click()

		submit_btn = self.driver.find_element_by_id('submit_btn')
		submit_btn.click()

		self.page = self.driver.page_source
		self.assertTrue("Your registration has been submitted!" in self.page)

		self._remove_test_user_from_db()

def test_redirect_to_registration_page(self):
		self.driver.get(S.HOME_PAGE)
		register_btn = self.driver.find_element_by_css_selector('#account_actions a')
		register_btn.click()

		self.page = self.driver.page_source
		self.assertTrue("Create a New Account" in self.page)


if __name__ == '__main__':
    unittest.main()

