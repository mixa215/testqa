from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "C:/Users/111/testqa/3.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, '1')
    input1.send_keys("Багдасарьян")
    input3 = browser.find_element(By.ID, '2')
    input3.send_keys("Михаил")
    input4 = browser.find_element(By.ID, '3')
    input4.send_keys("Владиславович")
    input5 = browser.find_element(By.NAME, 'email')
    input5.send_keys("qwe@mail.ru")
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="Student"]')
    option1.click()
    input2 = browser.find_element(By.ID, 'last_name')
    input2.send_keys("Petrov")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла