
''' Constants for all tests for RIDataHub
	
	Usage:
	*Be sure to change superuser and datahub user login info before testing
	*Change HOME_PAGE url to whichever version of datahub you're working off of (local or production) 
'''

#Admin login: 
SUPERUSER_USERNAME = 'ttest'
SUPERUSER_PASSWORD = 'password'

#DataHub User Login:
USER_LOGIN = 'username@test.com'
USER_PASSWORD = 'password'


HOME_PAGE = 'http://127.0.0.1:8000/'

#TestNewAccounts
ADMIN_LOGIN_PAGE = HOME_PAGE + 'admin/'
USERNAME_SEARCH_URL = HOME_PAGE + 'admin/auth/user/?q=test%40testspace.org'
NEW_ACCOUNT_PAGE = HOME_PAGE + 'accounts/register/'

#TestDataCatalogSearch
INDICATOR_SEARCH_URL = HOME_PAGE + 'dictionary/indicator-search/'

#TestAddDeleteIndicatorsToiLists
CATALOG_FILTER_URL = HOME_PAGE + 'dictionary/indicator-search/?text=Health&data_levels=School&data_sources=doh'

#TestCreateDeleteiLists & TestAddDeleteIndicatorsToiLists
USER_PORTFOLIO_URL = HOME_PAGE + 'accounts/portfolio/'