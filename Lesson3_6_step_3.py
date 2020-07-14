import pytest
import time
import math

from selenium import webdriver





@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
# def test_print(link):
#     print("asd" + link)

def test_right_answer(browser, link):
    answer = math.log(int(time.time()))
    answer3 = str(answe
    browser.get(link)
    browser.implicitly_wait(10)
    # time.sleep(5)
    # browser = webdriver.Firefox()
    browser.find_element_by_css_selector(".string-quiz__textarea").send_keys(answer3)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(3)
    answer2 = browser.find_element_by_css_selector(".smart-hints__feedback").text
    assert answer2 == "Correct!", "Value answer2= " + answer2


# time.sleep(10)
#     answer2 = str(answer)
#     qwe = browser.find_element_by_id("ember80")
#     qwe.send_keys(answer2)
#     browser.find_element_by_class_name("submit-submission").click()
#     time.sleep(3)
#     answer3 = browser.find_element_by_css_selector(".smart-hints__feedback").text
#     assert answer3 == "Corrrect!", answer3 + "Value"
