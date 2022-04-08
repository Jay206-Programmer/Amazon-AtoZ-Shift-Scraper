#* Library Imports
from selenium.webdriver.common.by import By
import time
import json

#* Relative Imports
from driver_utility import DriverUtility

#* Global Variable Initialization
with open("Auth.json",'r') as ro:
    AUTH_DICT = json.load(ro)
    
class HandleAtoZLogin:
    
    def __init__(self):
        self.ATOZ = DriverUtility("https://atoz.amazon.work/shifts/dashboard")
        self.login()
        self.ATOZ.get_driver().quit()
    
    def handle_initial_login_page(self):
        print("AtoZ Initial Login Page Encountered")
        self.ATOZ.find_and_write(By.ID, "login", AUTH_DICT['atoz-email'], wait=True)
        self.ATOZ.find_and_write(By.ID, "password", AUTH_DICT['atoz-pass'])
        self.ATOZ.find_and_click(By.ID, "buttonLogin")
        print("AtoZ Initial Login Page Complete")
        
    def handle_otp_page(self):
        print("OTP Page Encountered")
        self.ATOZ.find_and_click(By.XPATH, "//input[@value='1']", wait=True)
        self.ATOZ.find_and_click(By.ID, "buttonContinue")
        
        print("\n\nPlease Enter OTP: ")
        otp = input()
        # HandleGmailLogin()
        
        self.ATOZ.find_and_write(By.ID, "code", otp)
        self.ATOZ.find_and_click(By.ID, "buttonVerifyIdentity")
        
        self.ATOZ.find_and_click(By.CLASS_NAME, "atoz-find-shifts-quicklinks-button", wait=True)
        print("OTP Page Complete")
    
    def login(self):
        
        #* Handle Initila Login Page
        self.handle_initial_login_page()
        
        #* Handling OTP
        self.handle_otp_page()
        
        time.sleep(100)
    
class HandleGmailLogin:
    
    def __init__(self):
        self.GMAIL = DriverUtility("https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.login()
        
    
    def login(self):
        self.GMAIL.find_and_write(By.ID, "identifierId", AUTH_DICT['gmail-id'], wait=True)
        self.GMAIL.find_and_click(By.ID, "identifierNext")
        time.sleep(100)
    
if __name__ == "__main__":
    HandleAtoZLogin()
