from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import unittest


class ContactForm(object):

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
        value = WebDriverWait(
                    driver, 10).until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH, """//div/label[@for='new_client_message_first_name']/../../div[2]/div[position()=3 and text() ="can't be blank"]"""
                                )
                            )
                    )
        return value

    @staticmethod
    def is_empty_error_displayed_for_last_name(driver):
        value = WebDriverWait(
                    driver, 10).until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH, """//div/label[@for='new_client_message_last_name']/../../div[2]/div[position()=3 and text() ="can't be blank"]"""
                                )
                            )
                    )
        return value
