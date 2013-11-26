		
#unpacking from array that is returned from the findall method

		self.browser.get('http://ridatahub.org/about/')
		self.home_btn = browser.find_element_by_id('logo')
		self.home_btn.send_keys(Keys.RETURN)
		self.home_btn.click()


		''''http://ridatahub.org/about/' '''


	def Open_Page_And_Check_Hm_Btn1(self):	
		self.browser.get('http://ridatahub.org/about/')
		self.home_btn = browser.find_element_by_id('logo')
		self.home_btn.send_keys(Keys.RETURN)


	def test_open_page(self):
		login_btn = self.browser.find_element_by_id("weave_login_submit")
		self.assertEqual('go', login_btn.get_attribute('value'))

		#login_btn.click()

	def Open_Page_And_Check_Hm_Btn2(self):	
		self.browser.get('http://ridatahub.org/')
		login_btn = self.browser.find_element_by_id("weave_login_submit")
		login_btn.click()
	



		def test_user_portfolio_content(self):
		self._login()
		#self._sign_out()

		#manage_portfolio_option = self.browser.find_element_by_css_selector("#account_actions a")
		#self.assertEqual("Manage your Portfolio", manage_portfolio_option.text)

		self.page = self.browser.page_source
		your_ilist_found = re.search(r"Your", self.page)
		self.assertNotEqual(your_ilist_found, None)

		#your_ilist = self.browser.find_element_by_css_selector(".grid_12 h2")
		#your_ilist = self.browser.find_element_by_css_selector(content + "h2")




#create_btn = select_btn.send_commands(Commands.GET_ELEMENT_VALUE_OF_CSS_PROPERTY)		


		#iList_table = self.driver.find_element_by_css_selector("#portfolio_user_ilists tbody")
		#tr_tag = iList_table.find_element_by_tag_name("tr")
		#iList_to_delete = self.driver.find_element_by_id(tr_tag.id)