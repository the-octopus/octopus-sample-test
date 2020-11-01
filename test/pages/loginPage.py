
from selenium.webdriver.common.by import By
from Octopus.OctopusHTMLReport.OctopusReporter import Reporter
from Octopus.OctopusCore.selenium_extensions import (Click, findElementBy, isDisplayed,
                                     isEnabled, isSelected, sendKeys,
                                     waitUntilDisplay, waitUntilExistInDOM,
                                     waitUntilHidden,select,multi_select)

class LoginPage:
    driver = None
    def __init__(self,driver):
        self.driver = driver
    
    # https://www.codewars.com/users/sign_in
    # Locators Variables 
    userName = (By.ID, 'user_email')
    password = (By.ID,'user_password')
    loginError = (By.XPATH,'//div[contains(@class,"flash-msg error")]')
    submitButton = (By.XPATH,'//button[@type="submit"]')
    lstCountriesLocator = (By.XPATH,'//button[@type="submit"]')

    # http://192.168.45.201:8080/login?from=%2F
    # userName = (By.ID, 'j_username')
    # password = (By.NAME,'j_password')
    # loginError = (By.XPATH,'//div[contains(@class,"alert-danger")]')
    # submitButton = (By.XPATH,'//input[@type="submit"]')
    # lstCountriesLocator = (By.XPATH,'//input[@type="submit"]')

    # WebElements of the page
    txtUserName=None
    txtPassword=None
    btnSubmit=None
    lstCountries=None
    divNotifcation=None

    # setter method
    def set_userName(self, _userName):              
        self.txtUserName = self.driver.findElementBy(*LoginPage.userName)
        self.txtUserName.sendKeys(_userName)        

    # setter method
    def set_password(self, _password):
        self.txtPassword = self.driver.findElementBy(*LoginPage.password)       
        self.txtPassword.sendKeys(_password)        
        
    # setter method
    def click_submit(self):
        self.btnSubmit = self.driver.findElementBy(*LoginPage.submitButton)               
        self.btnSubmit.Click()
        
    # Test Method
    def login(self,tdr=dict()):        
        self.set_userName(tdr["userID"])
        self.set_password(tdr["Password"])        
        self.click_submit()

    # Login Assertion method    
    def login_error_displayed(self):
        self.divNotifcation = self.driver.findElementBy(*LoginPage.loginError)

        if self.divNotifcation.waitUntilDisplay(3):
            # report fail message to the HTMLReport and Console as well
            Reporter.failed("Login Failed for error : {0}".format(self.divNotifcation.text))
            Reporter.passed("")
            Reporter.error("")
            Reporter.info("")
            return False
        elif self.divNotifcation.waitUntilHidden(3):
            # report pass message to the HTMLReport and Console as well
            Reporter.passed("Login passed")
            return True
    