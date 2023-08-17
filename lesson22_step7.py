import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

input1 = browser.find_element(By.XPATH, '//*[@id="file"]')
input1.send_keys(file_path)

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()