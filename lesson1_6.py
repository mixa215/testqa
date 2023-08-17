import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')

# закрываем браузер после всех манипуляций
time.sleep(3)
browser.quit()