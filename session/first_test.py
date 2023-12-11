import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
#from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from  appium.webdriver.common.touch_action import TouchAction

#subprocess.Popen(['appium', 'server', '--address', '127.0.0.1', '--port', '4723', '--allow-cors'])
#time.sleep(10)
caps = {
  "appium:autoGrantPermissions": True,
  "appium:automationName": "uiautomator2",
  "appium:newCommandTimeout": "500",
  "appium:noSign": True,
  "platformName": "Android",
  "appium:platformVersion": "10",
  "appium:resetKeyboard": True,
  "appium:systemPort": "8301",
  "appium:takesScreenshot": True,
  "appium:appPackage": "com.ajaxsystems",
  "appium:appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
  "appium:deviceName": "emulator-5554"
}
capabilities_options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

driver.implicitly_wait(30)
time.sleep(3)

driver.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/text').click()
time.sleep(1)

elem_login = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')
elem_login.send_keys('qa.ajax.app.automation@gmail.com')


elem_password = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]')
elem_password.send_keys('qa_automation_password')


signIn = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
signIn.click()
time.sleep(4)

menu = driver.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/menuDrawer')
menu.click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]').click()

#driver.swipe(470, 1400, 470, 1200, 400)

#driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(text("Sign out"))')

touch = TouchAction(driver)
touch.press(x=354, y=595).move_to(x=354, y=300).release().perform()
time.sleep(5)

signOut = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Sign Out"]')
signOut.click()

time.sleep(7)
driver.quit()
