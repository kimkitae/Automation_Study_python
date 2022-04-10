from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = "10"
desired_caps["automationName"] = "uiautomator2"
desired_caps['uuid'] = "29c3433201017ece"
desired_caps['appActivity'] = "com.elevenst.intro.Intro"
desired_caps['appPackage'] = "com.elevenst"
desired_caps['unicodeKeyboard'] = "false"
desired_caps['resetKeyboard'] = "true"
desired_caps['noReset'] = "true"
desired_caps['systemPort'] = 8201
desired_caps['adbPort'] = 5039

driver = webdriver.Remote('http://localhost:7726/wd/hub', desired_caps)
driver.implicitly_wait(5)


driver.find_element(By.ID, "com.elevenst:id/btn_my").click()

time.sleep(2)
driver.find_element(By.XPATH, "//android.view.View[@content-desc='찜']").click()
time.sleep(3)
print(driver.page_source)
list = driver.find_elements(By.XPATH, "//*[@class='android.widget.ListView' and @index='3']/android.view.View")
time.sleep(2)
list[0].click()
time.sleep(2)


