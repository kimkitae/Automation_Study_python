from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = "10"
desired_caps["automationName"] = "uiautomator2"

desired_caps['appActivity'] = "com.campmobile.noon.ui.splash.SplashActivity"
desired_caps['appPackage'] = "com.campmobile.noon"
desired_caps['unicodeKeyboard'] = "false"
desired_caps['resetKeyboard'] = "true"
desired_caps['noReset'] = "true"

driver = webdriver.Remote('http://localhost:7725/wd/hub', desired_caps)
driver.implicitly_wait(5)
