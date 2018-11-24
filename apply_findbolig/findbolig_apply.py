## Scraper for findbolig

import os
from selenium import webdriver

class FindBoligApply():

    def __init__(self):
        self.header = '--headless'
        # Start driver with options
        fox_opt = webdriver.FirefoxOptions()
        fox_opt.add_argument(self.header)
        self.driver = webdriver.Firefox(firefox_options=fox_opt)

    # def apply_apartment(self, url):
    def login_findbolig(self, username, password):
        assert(username == str(username))
        assert(password == str(password))
        url = 'https://www.findbolig.nu/logind.aspx'

        self.driver.get(url)
        self.driver.find_element_by_xpath('//input[contains(@id, "UserName")]').send_keys(username)
        self.driver.find_element_by_xpath('//input[contains(@id, "Password")]').send_keys(password)
        self.driver.find_element_by_xpath('//a[contains(@id, "LoginShadow")]').click()
        try:
            print(self.driver.find_element_by_xpath('//h1[contains(text(), "Min side")]').text)
            login = True
        except:
            login = False
            self.close()

        return login

    def click_apply(self, url):
        self.driver.get(url)
        try:
            self.driver.find_element_by_xpath('//a[contains(@id, "Signup")]').click()
        except:
            print("The apply did not succeed!")
            self.close()

    def close(self):
        self.driver.quit()




