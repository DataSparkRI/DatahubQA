DataHub QA Testing
==================

Automated tests for Datahub.


Usage:
------------------

#####View requirements.txt before running tests

1. Within the settings file set a superuser username and password. This will allow the tests to run admin related tasks.

2. Within the settings file set the user login and password. This is for test that perform as a regular user of the site.

3. Within the settings file set the home page to whichever version of datahub you are testing (local or production).

4. Execute run_tests.sh to run all tests.
