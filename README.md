# The-Octopus-Test Sample Test Project.

[The-Octopus-Test] (https://pypi.org/project/the-octopus-test/) is a community driven tool  that is fully featured and that you can get started with in moments.

My goal is to make test automation easy, robust, independent and featured.

This simple documentation will help you with all the details you need to use **The-Octopus-Test Framework** to create effective test automation.

**The-Octopus-Test Framework** is a Hybrid test automation framework, that combines features of (Modular, Keyword Driven and Data driven).

- As of now, I'm using the **Microsoft excel Data Sheet** as a database source for the managment and control of **KeyWords** and **Execution Flow**.



## Basic Concepts :

* Data Driven: 
  - All test data is stored in Microsoft excel Data Sheet.

* Keyword Driven: 
  - Function names are stored in Microsoft excel Data Sheet as well some flages to control which function to be executed with which data source.

* Page Object pattern and Page Factory:
  - All test cases are written under the test/pages folder.
  - Each page/module has a separate file.
  - More details on the [POM ](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html)

* Common web page interaction methods:
  - Added selenium extensions class to give a custom functions like Click(), sendKeys() , etc... 

* Common Mobile App interaction methods.
  - to be added soon in next releases

* Objects shared repository:
  - I recommend creating a locatores module that hold individual classes for elements on an individual page to be shared on all pages

* Extent HTML Report template:
  - I used the most professional reporting tool, Extent HTML report as template to generate the test execution report. 



## Test Development :

Using  [The-Octopus-Test] (https://pypi.org/project/the-octopus-test/) framework is identical to using a Selenium Webdriver. 
Once you have installed the framework to your machine.
  - Importing the **Octopus.OctopusCore.driver** in your **main.py** , is enough to run the test.
  - Importing the **Octopus.OctopusHTMLReport.OctopusReporter** , is enough to start reporting info,pass,fail and error status.
  - Importing the **Octopus.OctopusCore.selenium_extensions** , is enough to start using the custom functions Click, findElementBy, sendKeys, waitUntilDisplay,..etc. 

### Test Project Folder Structure:

  - It is a **MUST** to, follow the same project structure and name of folders as bellow.
  - It is a **MUST** to,  Do Not change the name and path of **scenarios** folder, it should be  **test / scenarios / testScenarios.py**.
  - It is a **MUST** to,  Do Not change the name and path of **ControlFile.xlsx** folder, it should be  **resourcses / TestData / ControlFile.xlsx**.

  ```
  <Octopus_Sample_Test>
      +--------------------------+
      |                          |
      |                          |
      |<reports>                 |
      |                          |
      |<resourcses>              |                        
      |    <ChromeDriver>        |
      |    <ChromeDriver>        |
      |    <ChromeDriver>        |
      |    <ChromeDriver>        |
      |    <TestData>            |
      |       ControlFile.xlsx   |
      |<test>                    |                        
      |    <pages>               |
      |       loginPage.py       |
      |       homePage.py        |
      |       ....               |
      |       ....               |
      |    <scenarios>           |
      |       testScenarios.py   |
      |                          |
      |                          |
      |main.py                   |    
      |                          |
      |                          |
      |                          |
      +--------------------------+
  ```

  * **reports** folder :  It is auto created after test run and it contains a subfolders with time stamp for each run that has the **HTMLOctopusReport**.

  * **resources** folder :  Contains the test browsers extensions and the test data excel sheet as follow.
  - **ChromeDriver folder**: it contains the Chrome Driver extension.
  - **FireFoxriver folder**: it contains the FireFox Driver extension.
  - **IEdgeDriver folder**: it contains the Edge Driver extension.
  - **TestData folder**: it contains the test data excel sheet **ControlFile.xlsx**.

  * **test** folder : It hold all the testing related classes for individual pages and the test scenarios as well, It contains of 2 sub folders **pages** & **scenarios**.
  - **pages** folder: we are following the POM architicture pattern, so this folder contains a python module / file for each page from the application under test. 
  - **scenarios** folder: It Contains only 1 module/file with the name **testScenarios.py** , and this class is the one that holds the test scenario methods that will 
      be called by the driver module, these methods can combine more than one test method from different modules under the pages class.

  * **main .py**: This module is the main entry point for the execution.

  * In order to run our project from the command line as follow.
  - open command line.
  - cd to the folder contains the main .py.
  - run the command 
  ```
  python main.py 

  ```

### How to create a test class ?

  - Go to the folder **test / pages**.
  - Create a python file example **loginPage.py**.
  - In order to locate an element you have to import.
   ``` 
   from selenium.webdriver.common.by import By 
   ```
  - in order to interact with the element you have to import.
    ```
    from Octopus.OctopusCore.selenium_extensions import (Click, isEnabled, sendKeys,select,multi_select)
    ```
  - in order to syncronize the execution according to application reponse you have to import.
    ```
    from Octopus.OctopusCore.selenium_extensions import (isDisplayed,
                                      isEnabled, isSelected, 
                                      waitUntilDisplay, waitUntilExistInDOM,
                                      waitUntilHidden,select,multi_select)
    ```
  - in order to report the status about test stpes / cases you have to import.
    ```
    from Octopus.OctopusHTMLReport.OctopusReporter import Reporter
    ```
  - Sample test calss for a login page, that i recommend to follow the same.
  
    .. code-block:: python
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

            # Login assertion method    
            def login_error_displayed(self):
                self.divNotifcation = self.driver.findElementBy(*LoginPage.loginError)

                if self.divNotifcation.waitUntilDisplay(3):
                    # report fail message to the HTMLReport and Console as well
                    Reporter.failed("Login Failed for error : {0}".format(self.divNotifcation.text))
                    return False
                elif self.divNotifcation.waitUntilHidden(3):
                    # report pass message to the HTMLReport and Console as well
                    Reporter.passed("Login passed")
                    return True
      

  
### How to create a test method ?
  - Test method is a simple blind method that only interact with the application elements by Click(), sendKeys(), ..etc.
  - As we follow the DataDriven approche it is mandatory to pass dictionary data collection to the test method.
  - It is a MUST to use the dict() data collection, becuase it is a Key/Value data collection type.
  - Sample test method for a login test with the dict() data type variable, that i recommend to follow the same.

  .. code-block:: python
        # Test Method
        def login(self,tdr=dict()):        
            self.set_userName(tdr["userID"])
            self.set_password(tdr["Password"])        
            self.click_submit()


### How to pass the test data to a test method ?
  - In the framework I follow the **Data Driven** approch, and using the Microsoft excel Sheet as Data source.
  - Each application page/screen should have a separated data sheet in the **ControlFile.xlsx** file.
  - In order to pass test data to a test method, it is MUST to pass variable of type **dict()** to the method.
    ```
    def login(self,tdr=dict()):
    ```
  - Use the passed dict() parameter to test mthod, to get the values of the data field by the name of the field as in excel data sheet.
    ```
    self.set_userName(tdr["userID"])
    ```
  - In the ControlFile.xlsx file, create a data sheet that has a meaningful name as per the application page.
  - Create the sheet and set the first row in the sheet by column names.

  ![Sample Login Data Sheet](https://the-octopus.github.io/screenShots/login_sheet.png)


### How to use the OctopusHTMLReport to report status PASS/FAIL/ERROR/INFO ?
  - The OctopusHTMLReport has a set of functions to report status and statistics about the execution.
  - In order to use the reporting mechanism of the-octopus-test framework.

  .. code-block:: python
        # import the reporter class
        from Octopus.OctopusHTMLReport.OctopusReporter import Reporter

        # report info step in the report , without screen shot.
        Reporter.info(" details ")

        # report a success step in the report , witht screen shot.
        Reporter.passed(" details ")

        # report a failure step in the report , with screen shot.
        Reporter.failed(" details ")

        # report error step in the report , with screen shot.
        # it is reocmmended to use this method in the except: Block of a Try: Block
        Reporter.error(" details ")

  ![Sample report](https://the-octopus.github.io/screenShots/report.png)


### How to create a test scenario method in **testScenarios.py** ?
  - This Framework is implemented on a configurable / easy to use approach, so alot of things is done behinde the sceen.
  - The step of getting the test data from excel sheet and map it to the test scenario method.
  - The test data that was mapped in the **Driver** data sheet in the **ControlFile.xlsx** is loaded in the framework as dict() data type.
  - I have created **Octopus.OctopusCore.globals** class to hold all global shared resources like Browser, FrameworkPath.
  - The **Globals.Test.Browser** is to be used for initializing the page calss elements.
  - The the scenario method is a **MUST** to has a parameter of type dict() like **TestDataRow=dict()**.
  - Is a MUST to keep scenario method static method **@staticmethod**.
  - Is a MUST to keep the name of the class as **TestScenarios**.

  .. code-block:: python
        # import the octopus supportive classes
        # to report a status in the except: block
        from Octopus.OctopusHTMLReport.OctopusReporter import Reporter
        
        #inmport the test method / page class , for exmaple loginPage
        from test.pages.loginPage import LoginPage

        class TestScenarios:          
            @staticmethod
            def ValidateLogin(TestDataRow=dict()):
                try:
                  login_page = LoginPage(Globals.Test.Browser) # initailize object from the class loginPAge by passing the Browser.
                  login_page.login(TestDataRow) # passing the test data that is initialized in framework as per the driver data sheet configurations.
                  login_page.login_error_displayed()
                except Exception as error:            
                    Reporter.failed("Validate Login Failed for {0}".format(error)) #ValidateLogin
            
           
  ![Sample Driver Sheet Mapping](https://the-octopus.github.io/screenShots/driver_sheet.png)


### How to pass the test data to a test scenario method ?
  - Do the mapping between the test scenario method and the data sheet.
  - Copy the test **scenario method name** and put it in a new row in the **Driver** data sheet in the column **Function_Name**.
  - Put the data sheet name that will be used as source for that scenario in the **Driver** data sheet in the column **TestDataSheetName**.
  - Put the data sheet rows numbers in the **Driver** data sheet in the column **TestDataSheetRowNo**.
  - The data sheet row Nos, can be **range** like 1-10 , or can be **list** like 1,2,3,5,8 .

  ![Sample Driver Sheet Mapping](https://the-octopus.github.io/screenShots/driver_sheet.png)


### How to control the execution of the test scenarios methods from excel sheet **Driver**?
  - In the framework I follow the **KeyWord Driven** approch, and using the Microsoft excel Sheet as KeyWords source.
  - To control the execution flow of the test scenarios , use the **Driver** data sheet in the **ControlFile.xlsx**.
  - implement the driver data sheet by doing the mapping between scenarios test methods name and the data sheet.
  - Control the execution by select the value **Yes** or **No** from the column **Execution_Flag**. 


### How to configure the environment settings Browser name, project name, URL from excel sheet **Environment**?
  - The Framework is implemented as configurable.
  - To configure the environment details please use the **Environment** data sheet in the **ControlFile.xlsx**. 
    - **RunEnvironment** :	WEB / MOBILE
    - **RunType** :	Execution / Debug
    - **ProjectName** : the_Octopus_Test
    - **Explorer**:	CHROME / IE / FIREFOX
    - **URL** :	https://www.codewars.com/users/sign_in

  ![Sample Driver Sheet Mapping](https://the-octopus.github.io/screenShots/Environment_sheet.png)


### How to create a test data sheet for a page in your application, exmaple login page ?
  - Each test method / application page should have a separated data sheet.
  - Dat sheet structure is recommened to be like the bellow screen.
  - first column is the **RowID** of the data rows in the sheet.
  - second column is the **LoginRow** to refrence the login data row from the login data sheet.
  - third column is the **TestCaseDescription** to set a discription about the test case executed by this data row.
  - fourth column is the **ExpectedResult** to give an exepected result for that data row.
  - rest of the sheet is column names like the fields on the application page.

  ![Sample Data Sheet](https://the-octopus.github.io/screenShots/sample_data_sheet.png)


### How to manage the login accounts for test data, exmaple selecting a login data for a specified scenario ?
  - In order to map a login account to a specific test case / test data row.
  - in the test data sheet make sure to let the second column name is **LoginRow** .
  - put in that column the value of the row number from login sheet.
  - use this value in you code to get the test login data from data sheet as follow.
  - the **DataManager** class from the **Octopus.OctopusCore.dataManager** contains methods to get data from excel sheet.

  .. code-block:: python
        # import the octopus DataManager class
        from Octopus.OctopusCore.dataManager import DataManager
        
        # define a variable and use the getDictionaryTableFromexcel method to get a dict() data type
        # the index [0] means get only the first row from the returened set of rows.
        LoginRow = DataManager.getDictionaryTableFromexcel("select * from ["Login"$] where RowID=" + rowNum )[0] 


## How to link the developed test scneario method from the  **testScenarios.py** to the **ControlFile.xlsx**
  - first of all We are passing a data collection of type dict() that will provide test data to test methods in **testScenarios.py**.
  - The name of the test data variables is defined as per the name of column in the test data excel sheet **ControlFile.xlsx**.
  - after define the test method in test scenario class , copy this name and put in the excel sheet **Driver** in the workbook file **ControlFile.xlsx**.



## Example used in this project:
I'm using the login page for the [www.codewars.com](https://www.codewars.com/users/sign_in). 

  - I defined the web elements of the login page in the class **LoginPage**  under file. 

    > test/pages/loginPage.py

  - I defined the test scenario method of login page in the class **TestScenarios**  under file.

    > test/scenarios/testScenarios.py

  - Test data is defined in the excel sheet under the 

    > Resources/TestData/ControlFile.xlsx

  - Browsers derives is stored under the path 

    > Resources/ChromeDriver/chromedriver.exe


### Running the test:
 1. Define the web elements and create the test method as per the loginpage under test/pages/loginPage.py
 2. Make sure to use pass a data collection of type dictionary dict() to the test method.
 3. define a test scenario method as per the ValidateLogin example under test/scenarios/testScenarios.py
 4. Configure the Excel Control file , Driver sheet with the name of your test scenario method as per the example under 
  > Resources/TestData/ControlFile.xlsx
 5. Define your test data as in Excel Control file , Login sheet as per the Login sheet under Resources/TestData/ControlFile.xlsx
 6. Make sure to use the column names in Login sheet to be same names you are using in the data dictionary passed to the test method.
 7. Save all you work.
 8. run the test by using the command.
    ```
    python main.py 

    ```
 9. The system will run the test and generate a HTML report with date and time stamp name as per the bellow example.
  > Reports/Automation_Result_timestamp/Automation_Report_projectName.html
 

## Please for more details do not hesitate to contact me at [LinkedIn](https://www.linkedin.com/in/abdelghany-abdelaziz)