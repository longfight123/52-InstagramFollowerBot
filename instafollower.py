from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os

load_dotenv('.env')
INSTAGRAM_USER = os.getenv('INSTAGRAM_USER')
INSTAGRAM_PW = os.getenv('INSTAGRAM_PW')
INSTAGRAM_EMAIL = os.getenv('INSTAGRAM_EMAIL')
TARGET_ACCOUNT = 'kimkardashian'


class InstaFollower:
    """
    A class used to manage the browser to follow instagram users.

    ...

    Attributes
    ----------
    driver: WebDriver
        a tool for automated testing of webapps across browsers

    Methods
    -------
    login()
        log into the user's instagram account
    find_followers()
        finds other instagram users from the target account
    follow()
        follows other instagram users that the user is not
        currently following
    """

    def __init__(self, path):
        """
        Parameters
        ----------
        path : str
            The file system path to the WebDriver
        """

        self.driver = webdriver.Chrome(path)
        self.driver.get('https://www.instagram.com')
        time.sleep(3)

    def login(self):
        """log into the user's instagram account
        """

        username_element = self.driver.find_element_by_name('username')
        username_element.send_keys(INSTAGRAM_USER)
        password_element = self.driver.find_element_by_name('password')
        password_element.send_keys(INSTAGRAM_PW)
        login_button = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
        login_button.click()
        time.sleep(3)

    def find_followers(self):
        """finds other instagram users from the target account
        """

        self.driver.get(f'https://www.instagram.com/{TARGET_ACCOUNT}/')
        time.sleep(3)
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(5)
        for i in range(10):
            self.follow()
            scroll_element = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
            time.sleep(2)

    def follow(self):
        """follows other instagram users that the user is not
        currently following
        """

        follow_button_elements = self.driver.find_elements_by_class_name('y3zKF')
        for follow in follow_button_elements:
            try:
                follow.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_css_selector('body > div:nth-child(19) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
                cancel_button.click()
                time.sleep(1.5)

