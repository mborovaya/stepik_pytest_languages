from selenium.webdriver.remote.errorhandler import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_exists(browser):
    browser.get(link)
    #time.sleep(30)
    try:
        assert browser.find_element_by_css_selector("[data-loading-tex]")

    except NoSuchElementException:
        assert False, "Cannot find 'Add to cart button'"
