import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from tests.ContactForm import ContactForm
MessageField = ContactForm.MessageField
FirstNameField = ContactForm.FirstNameField
LastNameField = ContactForm.LastNameField
EmailField = ContactForm.EmailField


import unittest



class TestContactForm(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        fn = os.path.join(os.path.dirname(__file__))
        print(fn)
        self.driver = webdriver.Chrome(fn + '/../chromedriver_win32/chromedriver.exe')
        self.driver.get("http://test.must.com.ua/")
    # def tearDown(self):
    #     self.driver.close()

    def test_empty_fields(self):
        driver = self.driver


# open form
        contact_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.livesite-contact.ls-action")))
        contact_button.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ls_cboxLoadedContent"]/iframe""")))
# submit form with empty values
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ls_cboxLoadedContent"]/iframe"""))
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Send Message']")))
        submit_button.click()
# verify errors

        self.assertTrue(ContactForm.is_empty_error_displayed_for_message(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_email(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_first_name(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_last_name(driver))

    def test_different_names_error(self):
        driver = self.driver
        contact_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.livesite-contact.ls-action")))
        contact_button.click()
        ContactForm.focus(driver)
        FirstNameField.find(driver).send_keys("name")
        LastNameField.find(driver).send_keys("name")
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Send Message']")))
        submit_button.click()
        # проверка ошибки, что имья и фамилия не должны совпадать
        self.assertTrue(ContactForm.is_first_last_not_different_errors_displayed(driver))
        # проверка ошибок пустых полей
        self.assertTrue(ContactForm.is_empty_error_displayed_for_message(driver))
        self.assertTrue(ContactForm.is_empty_error_displayed_for_email(driver))
        # не должно быть ошибки о пустых полях для фамилии, имени
        self.assertFalse(ContactForm.is_empty_error_displayed_for_first_name(driver))
        self.assertFalse(ContactForm.is_empty_error_displayed_for_last_name(driver))












