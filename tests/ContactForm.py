from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import unittest



class ContactForm(object):

    class MessageFieldWithError(object):
        locator = """//div/label[@for='new_client_message_message']/../../div[2]/div[position()=1]/textarea"""

        @staticmethod
        def find(cls, driver):
            driver.find_element_by_xpath(cls.locator)

    class MessageField(object):
        locator = """//div/label[@for='new_client_message_message']/../../div[3]/div[1]/textarea"""

        @classmethod
        def find(cls, driver):
            return driver.find_element_by_xpath(cls.locator)

    class EmailField(object):
        locator = """//*[@id="new_client_message_email"]"""

        @classmethod
        def find(cls, driver):
            return driver.find_element_by_xpath(cls.locator)

    class FirstNameField(object):
        locator = """//*[@id="new_client_message_first_name"]"""

        @classmethod
        def find(cls, driver):
            return driver.find_element_by_xpath(cls.locator)

    class LastNameField(object):
        locator = """//*[@id="new_client_message_last_name"]"""

        @classmethod
        def find(cls, driver):
            return driver.find_element_by_xpath(cls.locator)

    form_locator = """//*[@id="ls_cboxLoadedContent"]/iframe"""

    @staticmethod
    def is_empty_error_displayed_for_message(driver):

        value = WebDriverWait(
                    driver, 10).until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH, """//div/label[@for='new_client_message_message']/../../div[2]/div[position()=2  and text()="can't be blank"]"""
                                )
                            )
                    )
        return value

    @staticmethod
    def is_empty_error_displayed_for_email(driver):
        value = WebDriverWait(
                    driver, 10).until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH, """//div/label[@for='new_client_message_email']/../../div[2]/div[position()=3 and text() ="can't be blank"]"""
                                )
                            )
                    )
        return value

    @staticmethod
    def is_empty_error_displayed_for_first_name(driver):
        try:
            value = WebDriverWait(
                        driver, 5).until(
                                EC.presence_of_element_located(
                                    (
                                        By.XPATH, """//div/label[@for='new_client_message_first_name']/../../div[2]/div[position()=3 and text() ="can't be blank"]"""
                                    )
                                )
                        )
            return value
        except:
            return False

    @staticmethod
    def is_empty_error_displayed_for_last_name(driver):
        try:
            value = WebDriverWait(
                        driver, 5).until(
                                EC.presence_of_element_located(
                                    (
                                        By.XPATH, """//div/label[@for='new_client_message_last_name']/../../div[2]/div[position()=3 and text() ="can't be blank"]"""
                                    )
                                )
                        )
            return value
        except:
            return False

    @staticmethod
    def is_first_last_not_different_errors_displayed(driver):


        value1 = WebDriverWait(
                    driver, 10).until(
                            EC.element_to_be_clickable(
                                (
                                    By.XPATH, """//div/label[@for='new_client_message_first_name']/../../div[2]/div[position()=3 and text() ="First name and last name must be different"]"""
                                )
                            )
                    )
        value2 = WebDriverWait(
                    driver, 10).until(
                            EC.element_to_be_clickable(
                                (
                                    By.XPATH, """//div/label[@for='new_client_message_last_name']/../../div[2]/div[position()=3 and text() ="First name and last name must be different"]"""
                                )
                            )
                    )
        value = value1 and value2
        print(value)
        return value

    @staticmethod
    def focus(driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="ls_cboxLoadedContent"]/iframe""")))
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ls_cboxLoadedContent"]/iframe"""))


