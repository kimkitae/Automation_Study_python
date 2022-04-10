from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException




desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = "12"
desired_caps["automationName"] = "uiautomator2"

desired_caps['appActivity'] = "com.campmobile.noon.ui.splash.SplashActivity"
desired_caps['appPackage'] = "com.campmobile.noon.debug"
desired_caps['unicodeKeyboard'] = "false"
desired_caps['resetKeyboard'] = "true"
desired_caps['noReset'] = "false"

driver = webdriver.Remote('http://localhost:7725/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//android.view.View[@content-desc='전체보기']").click()  # 약관보기
driver.find_element(By.XPATH,"//android.widget.Button[@resource-id='close-plc']").click() #약관닫기

time.sleep(2)

actions = TouchAction(driver)
actions.tap(None,803,620,1)
actions.perform() # 위치기반 서비스 이용약관 동의

driver.find_element(By.XPATH,"//android.widget.Button[@text='다음']").click()  # 다음버튼
driver.find_element(By.XPATH,"//android.widget.TextView[@text='나중에 하기']").click()  # 나중에하기
driver.find_element(By.XPATH,"//android.widget.Button[@text='확인']").click()  # 위치권한 확인
time.sleep(2)
driver.find_element(By.XPATH,"//android.widget.Button[@text='확인']").click()  # 접근권한 확인
driver.find_element(By.XPATH,"//android.widget.Button[@text='앱 사용 중에만 허용']").click()  # 위치 액세스
driver.find_element(By.XPATH,"//android.widget.Button[@text='앱 사용 중에만 허용']").click()  # 오디오 액세스
time.sleep(3)
try :
    driver.find_element(By.XPATH,"//android.widget.Image[@text='닫기']").click()  # 이벤트팝업 닫기
except NoSuchElementException :
    pass
driver.find_element(By.XPATH,"//android.widget.TextView[@text='카페/디저트']").click()  # 매장선택
time.sleep(2)
driver.find_element(By.XPATH,"//android.widget.TextView[@text='먹고 갈게요']").click()  # 팝업 먹고갈게요 선택
time.sleep(2)
driver.find_element(By.XPATH,"//android.widget.RadioButton[@text='포장 할게요']").click()  # 포장할게요 선택
driver.find_element(By.XPATH,"//*[@class='android.widget.ListView' and @index='0']/android.view.View[1]/android.view.View").click()  # 메뉴선택
driver.find_element(By.XPATH,"//android.view.View[@text='선택']").click()  # 옵션1 선택
driver.find_element(By.XPATH,"//android.widget.CheckedTextView[@text='HOT']").click()  # 옵션2 선택
driver.find_element(By.XPATH,"//android.widget.Button[@text='담기']").click()  # 담기 선택
driver.find_element(By.XPATH,"//android.widget.EditText[@index='0']").send_keys('kdaek88@gmail.com')  # 아이디 입력
driver.find_element(By.XPATH,"//android.widget.EditText[@index='1']").send_keys('test')  # 비밀번호 입력
time.sleep(2)
driver.find_element(By.XPATH,"//android.widget.Button[@text='로그인']").click()  # 로그인
driver.find_element(By.XPATH,"//android.widget.TextView[@text='포장 할게요']").click()  # 팝업 포장할게요 선택

driver.find_element(By.XPATH,"//*[@class='android.widget.ListView' and @index='0']/android.view.View[1]/android.view.View").click()  # 메뉴선택
driver.find_element(By.XPATH,"//android.view.View[@text='선택']").click()  # 옵션1 선택
driver.find_element(By.XPATH,"//android.widget.CheckedTextView[@text='HOT']").click()  # 옵션2 선택
driver.find_element(By.XPATH,"//android.widget.Button[@text='담기']").click()  # 담기 선택
time.sleep(2)
driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'건 결제하기')]").click()  # N건 결제하기 선택
driver.find_element(By.XPATH,"//android.widget.CheckBox[@index='0']").click()  # 결제동의 체크 선택
driver.find_element(By.XPATH,"//android.widget.Button[@text='결제하기']").click()  # 결제하기 선택
driver.find_element(By.XPATH,"//android.widget.Button[@text='다음']").click()  # 다음 선택


assert driver.find_element(By.XPATH,"//android.widget.TextView[@text='접수 대기중']").is_displayed(), "접수 대기중"

driver.find_element(By.XPATH,"//android.widget.Button[@text='주문 내역 보기']").click()  # 주문내역 보기 선택

time.sleep(2)
print(driver.page_source)

