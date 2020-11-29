from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains




driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost:63342/OC-App-master/OC-App-master/index.html?_ijt=u2sqgju0v816qpgh79tqa3q96v')
# Title verification
expectedTitle = "Online Community"
actualTitle = driver.title
print(driver.title)
if expectedTitle == actualTitle:
    print("Title verification Passed")
else:
    print("Title Verification Failed")
assert "No results found." not in driver.page_source
# login use case
# navigation use case
#driver.navigate
# locating HTML elements



#action on HTML elements

elem = driver.find_element_by_name("s_email")
elem.send_keys("abc@gmail.com")
elem = driver.find_element_by_name("s_password")
elem.send_keys("abcdef!")
elem = driver.find_element_by_id('login').click()

'''
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
'''
# confirm change in url
print(driver.current_url)

driver.close()
