from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = "12"
desired_caps["automationName"] = "uiautomator2"
desired_caps['uuid'] = "R3CN5056PGL"
desired_caps['appActivity'] = "com.dalkomm.beatorder.presentation.v3.intro.IntroActivity"
desired_caps['appPackage'] = "com.dalkomm.beatorder.debug"
desired_caps['unicodeKeyboard'] = "false"
desired_caps['resetKeyboard'] = "true"
desired_caps['noReset'] = "true"
desired_caps['mockLocationApp'] = "com.gsmartstudio.fakegps"

driver = webdriver.Remote('http://localhost:7725/wd/hub', desired_caps)
driver.implicitly_wait(5)

time.sleep(5)