import time
from selenium import webdriver


#from pytest_bdd import *
from behave import *

path = "C:/Python37/chromedriver.exe"

@given('login window')
def login_windows(context):
    #initiate driver
    context.driver=webdriver.Chrome(executable_path=path)
    context.driver.get("https://www.flipkart.com/")
    time.sleep(4)

@when('click on X')
def close_window(self):
    #Enter text and click for search
    self.driver.find_element_by_xpath("(//body[@class='fk-modal-visible']//button)[2]").click()


@when('enter product and click to search')
def enter_details(self):
    self.driver.find_element_by_name("q").send_keys("Iphone")
    self.driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)


@then(u'number of products')
def products_displayed(self):
    #display count and list of items
    resultcount = self.driver.find_elements_by_xpath("//div[contains(@class,'_3wU53n')]")
    print(len(resultcount))
    for item in resultcount:
        print(item.text)

