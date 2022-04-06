from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = "8"
desired_caps["automationName"] = "uiautomator2"
desired_caps['uuid'] = "2be02f89ec1d7ece"
desired_caps['appActivity'] = "kr.co.yogiyo.riderapp.ui.MainActivity"
desired_caps['appPackage'] = "kr.co.yogiyo.riderapp"
desired_caps['unicodeKeyboard'] = "false"
desired_caps['resetKeyboard'] = "true"
desired_caps['noReset'] = "true"
desired_caps['mockLocationApp'] = "com.gsmartstudio.fakegps"

driver = webdriver.Remote('http://localhost:7725/wd/hub', self.desired_caps)
driver.implicitly_wait(5)
