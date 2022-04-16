#* Library Imports
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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
        self.findShifts()
        
        time.sleep(100)
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

        print("OTP Page Complete")
        
        self.ATOZ.find_and_click(By.CLASS_NAME, "atoz-find-shifts-quicklinks-button", wait=True)
    
    def login(self):
        
        #* Handle Initila Login Page
        self.handle_initial_login_page()
        
        #* Handling OTP
        self.handle_otp_page()
        
    def handle_bs4(self, page_source):
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # with open("source.txt", 'wt', encoding='utf-8') as html_file:
        #     for line in soup.prettify():
        #         html_file.write(line)
        days = []
        days_selector = soup.find_all('button', class_='dayButton')

        for day_selector in days_selector:
            available_day_div = day_selector.find('span', class_ = "badge")
            if available_day_div is not None:
                final_date = ""
                date = day_selector.find("span", class_ = "atoz-date-string-full").find_all("div")
                for dt in date:
                    final_date += dt.get_text()
                days.append(final_date)
        
        return days
        
    def findShifts(self):
        
        print("Find Shifts Started")
        
        #* Get Page Source
        source = self.ATOZ.get_page_source()
        print(source)
        
        #* Handover to BS4
        print(self.handle_bs4(source))
        
    
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
