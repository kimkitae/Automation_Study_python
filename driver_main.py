from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
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
# 주문하기 클릭
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/fab").click()

# 비로그인 상태에서 매장 찾기 즐겨찾기 클릭 후 로그인
# print(driver.page_source)
# print(driver.context)
driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/action_store").click()
time.sleep(2)
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/action_user").click()
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/action_other").click()
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/tv_favorite").click()
# 루시(개발망) 매장 선택
store_lists = driver.find_elements(By.ID, "com.dalkomm.beatorder.debug:id/cl_card")
store_lists[0].click()
# 주문하러 가기 버튼 클릭
driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/btn_confirm").click()
time.sleep(2)
# 핫 아메리카노 클릭
menu_list = []

try:
    for i in range(1, 3) :
        menu_list.append(driver.find_element(By.XPATH,
                                         f"//*[@class='android.view.View' and @resource-id='beatContent']/android.view.View[@index='0']/android.view.View[@index='{i}']/android.widget.TextView[@index='2']"))
except NoSuchElementException:
    menu_list.append(driver.find_element(By.XPATH,
                                         f"//*[@class='android.view.View' and @resource-id='beatContent']/android.view.View[@index='0']/android.view.View[@index='1']/android.widget.TextView[@index='2']"))

time.sleep(3)
menu_list[0].click()
# 결제하기 버튼 클릭
time.sleep(3)
driver.find_element(By.XPATH, "//android.widget.Button[@text='결제하기']").click()

# 매장 찾기 > 즐겨찾기 선택
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/iv_favorite").click()

# 로그인 화면에서 ID/PW 입력 후 로그인 버튼 선택
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/et_id").send_keys("hjdev@beat.com")
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/et_pwd").send_keys("asdf1234")
# driver.find_element(By.ID, "com.dalkomm.beatorder.debug:id/btn_login").click()

time.sleep(5)
