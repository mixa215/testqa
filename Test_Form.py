from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import openpyxl

b = []
c = []
d = []
e = []
f = []
g = []
h = []

i=0
wb = openpyxl.reader.excel.load_workbook(filename="Pairwise.xlsx", data_only=True)
    
wb.active = 0
sheet = wb.active

for i in range(2,38):
    b.append(sheet['B'+str(i)].value)
    c.append(sheet['C'+str(i)].value)
    d.append(sheet['D'+str(i)].value)
    e.append(sheet['E'+str(i)].value)
    f.append(sheet['F'+str(i)].value)
    g.append(sheet['G'+str(i)].value)
    h.append(sheet['H'+str(i)].value)
for i in range(2,38):
    try: 
        link = "file:///C:/Users/111/testqa/%D1%84%D0%BE%D1%80%D0%BC%D0%B0.html"
        browser = webdriver.Chrome()
        
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.NAME, "FIO")
        input1.send_keys(b[i])
        input2 = browser.find_element(By.NAME, "email")
        input2.send_keys(c[i])
        input3 = browser.find_element(By.NAME, "Phone")
        input3.send_keys(d[i])
        select1 = Select(browser.find_element(By.NAME, "transfer"))
        select1.select_by_value(e[i])
        select2 = Select(browser.find_element(By.NAME, "HowManyPeople"))
        select2.select_by_value(f'{f[i]}')
        select3 = Select(browser.find_element(By.NAME, "HowManyChild"))
        select3.select_by_value(f'{g[i]}')


        input4 = browser.find_element(By.NAME, "ChildAge")
        input4.send_keys(h[i])



        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()