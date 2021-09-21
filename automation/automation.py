import os 
from selenium import webdriver

dirname = os.path.dirname(__file__)
driver_path = dirname + '/chromedriver.exe'

chrome_browser = webdriver.Chrome(driver_path)
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Selenium Easy Demo' in chrome_browser.title)
button_text = chrome_browser.find_element_by_class_name("btn-default")
print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Hey! I am automating this.')
button_text.click()

# chrome_browser.quit()
