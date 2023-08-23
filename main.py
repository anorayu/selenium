from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://dribbble.com/tags/financial%20forecast')

heading1 = driver.find_element(By.TAG_NAME, 'h1')
print(heading1.text)
# Find element by Tag Name
# my_div = driver.find_element(By.TAG_NAME, 'div')
# print(my_div.get_attribute("outerHTML"))

# Close the driver
driver.quit()





