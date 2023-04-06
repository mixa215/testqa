from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "C:/Users/111/testqa/3.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, 'input:nth-child(1)')
    a.send_keys("Багдасарьян")
    b = browser.find_element(By.CSS_SELECTOR, 'form>input:nth-of-type(2)')
    b.send_keys("Михаил")
    input4 = browser.find_element(By.CSS_SELECTOR, 'form>input:nth-of-type(3)')
    input4.send_keys("Владиславович")
    input5 = browser.find_element(By.CLASS_NAME, 'email')
    input5.send_keys("kate@mail.ru")
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="Student"]')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '[value="russian"]')
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, '[value="english"]')
    option3.click()
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