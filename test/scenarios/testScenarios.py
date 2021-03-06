
from Octopus.OctopusHTMLReport.OctopusReporter import Reporter
from Octopus.OctopusCore.globals import Globals
from test.pages.loginPage import LoginPage




class TestScenarios:

    @staticmethod
    def ValidateLogin(TestDataRow=dict()):
        try:
           login_page = LoginPage(Globals.Test.Browser)
           login_page.login(TestDataRow)
           login_page.login_error_displayed()
        except Exception as error:            
            Reporter.failed("Validate Login Failed for {0}".format(error)) #ValidateLogin
    
    @staticmethod
    def ValidateLoginTest(TestDataRow=dict()):
        try:
           login_page = LoginPage(Globals.Test.Browser)
           login_page.login(TestDataRow)
           login_page.login_error_displayed()
        except Exception as error:            
            Reporter.failed("Validate Login Test Failed for {0}".format(error)) #ValidateLoginTest