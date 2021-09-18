import selenium
from password import password , email
from selenium import webdriver
from time import sleep
#https://chromedriver.chromium.org/

l_url = "https://www.facebook.com/login.php"
class Facebook():

    def __init__(self , email , password):
        self.email= email
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.get(l_url)
        sleep(2)
        self.login()

    def login(self):

        bt1 = self.driver.find_element_by_xpath("//*[@title=\"Alle akzeptieren\"]")
        bt1.click()
        sleep(2)
        email_element = self.driver.find_element_by_id("email")
        email_element.send_keys(self.email)

        password_element =self.driver.find_element_by_id("pass")
        password_element.send_keys(self.password)

        bt2 = self.driver.find_element_by_id("loginbutton")
        bt2.click()


if __name__ == '__main__':
    login = Facebook(email = email , password= password)
        