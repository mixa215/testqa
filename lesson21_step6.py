from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()

    img1 = browser.find_element(By.ID, 'treasure')
    img1_valuex = img1.get_attribute("valuex")
    vluex = calc(img1_valuex)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(vluex)

    # people_radio = browser.find_element(By.ID, "peopleRule")

    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()