from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://automationexercise.com/")
driver.find_element_by_xpath("//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a").click()
driver.quit()


