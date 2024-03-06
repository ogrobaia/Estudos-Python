from selenium import webdriver 

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.google.com/")

# Abre uma nova aba
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 



