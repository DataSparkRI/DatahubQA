try: 
	import settings as S
except:
	ImportError
	sys.stderr.write("Error: Cannot find the 'settings.py' file")



"""
	Commonly used routines for RIDataHub's Selenium QA testing.
"""

def login(driver):
	username_field = driver.find_element_by_id("weave_login_username")
	username_field.send_keys(S.USER_LOGIN)

	username_field = driver.find_element_by_id("weave_login_password")
	username_field.send_keys(S.USER_PASSWORD)

	login_submit_btn = driver.find_element_by_id("weave_login_submit")
	login_submit_btn.click()

def sign_out(driver):
	sign_out_btn = driver.find_element_by_css_selector("#account_actions .submit_form")
	sign_out_btn.click()

def input_filters():
	terms_field = self.browser.find_element_by_id("indicator_field_text_search")
	terms_field.send_keys("health")

	data_level_ckbx = self.browser.find_element_by_id("id_data_levels_0")
	data_level_ckbx.click()

	data_source_ckbx = self.browser.find_element_by_id("id_data_sources_1")
	data_source_ckbx.click()

def create_iList(driver):
	driver.get(S.USER_PORTFOLIO_URL )

	new_ilist_btn = driver.find_element_by_id("new_ilist_button")
	new_ilist_btn.click()

	ilist_test_txt = "Test-iList"
	iList_name_input = driver.find_element_by_id("id_ilist_name")
	iList_name_input.send_keys(ilist_test_txt)

	create_btn = driver.find_element_by_css_selector("#new_ilist .button")
	create_btn.click()
