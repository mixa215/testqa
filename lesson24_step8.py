from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
h5 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной

assert "successful" in message.text