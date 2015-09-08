from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from tests.ContactForm import ContactForm


import unittest



class TestContactForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_empty_fields(self):
        driver = self.driver
        driver.get("http://test.must.com.ua/")

# open form
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.livesite-contact.ls-action")))
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ls_cboxLoadedContent"]/iframe""")))
# submit form with empty values
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ls_cboxLoadedContent"]/iframe"""))
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Send Message']")))
        submit_button.click();
# verify errors
        #driver.find_element_by_xpath("""//div/label[@for='new_client_message_message']/../../div[2]/div[position()=2  and text()="can't be blank"]""")
        # self.assertTrue(
        #                 WebDriverWait(
        #                             driver, 10).until(
        #                                                 EC.presence_of_element_located(
        #                                                     (
        #                                                         By.XPATH, """//div/label[@for='new_client_message_message']/../../div[2]/div[position()=2  and text()="can't be blank"]"""
        #                                                     )
        #                                                 )
        #                 )
        # )
        #
        self.assertTrue(ContactForm.is_empty_error_displayed_for_message(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_email(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_first_name(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_last_name(driver))
        #is_error_message_displayed(driver)

# def tearDown(self):
#     self.driver.close()






