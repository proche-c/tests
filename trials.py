
from selenium import webdriver
PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"

driver = webdriver.Chrome(PATH)

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome()
driver.get("https://www.apple.com/es/")
print(dir(driver))
driver.quit()