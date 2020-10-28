from selenium import webdriver
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

    userNameElement=None
    pwordElement=None
    submitBttn=None
    lstCountries=None
    notifcationElement=None
   

   # Example to explain how to use the select method

    def select_country(self, strCountry):              
        # userNameElement = self.driver.find_element(*LoginPage.userName)
        lstCountries = self.driver.findElementBy(*LoginPage.lstCountriesLocator)
        lstCountries.select(strCountry)
        
   
    def set_userName(self, _userName):              
        # userNameElement = self.driver.find_element(*LoginPage.userName)
        self.userNameElement = self.driver.findElementBy(*LoginPage.userName)
        self.userNameElement.sendKeys(_userName)
        
    
    
    def login_error_displayed(self):
        self.notifcationElement = self.driver.findElementBy(*LoginPage.loginError)
        
        if self.notifcationElement.waitUntilDisplay(3):
            Reporter.failed("Login Failed for error : {0}".format(self.notifcationElement.text))
            return False
        elif self.notifcationElement.waitUntilHidden(3):
            Reporter.passed("Login passed")
            return True
    
    
    def set_password(self, _password):
        self.pwordElement = self.driver.findElementBy(*LoginPage.password)       
        self.pwordElement.sendKeys(_password)        
        
        
    def click_submit(self):
        self.submitBttn = self.driver.findElementBy(*LoginPage.submitButton)               
        self.submitBttn.Click()
        
        
    def login(self,tdr=dict()):        
        self.set_userName(tdr["userID"])
        self.set_password(tdr["Password"])        
        self.click_submit()
