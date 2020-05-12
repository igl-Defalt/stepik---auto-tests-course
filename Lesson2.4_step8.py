from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = browser.find_element_by_id("book")
    btn.click()

    x = browser.find_element_by_id("input_value")
    x_element = x.text
    y = calc(x_element)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    btn_submit = browser.find_element_by_id("solve")
    btn_submit.click()

finally:
    time.sleep(10)
    browser.quit()
