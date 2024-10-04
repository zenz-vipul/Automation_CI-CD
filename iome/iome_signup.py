import time
from selenium import webdriver
import pytest
import random
import string
from selenium.webdriver.common.by import By

class Test_sign_up:

    @pytest.fixture()
    def test_invoke(self):
        self.driver = webdriver.Chrome()
        #self.driver.get('https://qadashboard.iome.ai/')
        self.driver.get('https://iome.ai')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button').click()

    @pytest.mark.flaky(rerun=2)
    def test_createnew(self,test_invoke):
        username = ''.join(random.choices(string.ascii_lowercase, k=5))
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password_length=10
        password=''.join(random.choices(password_characters,k=password_length))
        while not any(char.isdigit() for char in password) or not any(char.islower() for char in password) or not any(char.isupper() for char in password):
            password = ''.join(random.choices(password_characters, k=password_length))
        time.sleep(1)
        print(username)
        print(password)
        #sign up page
        self.driver.find_element(By.LINK_TEXT, 'Create new.').click()
        time.sleep(2)
        check=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[2]/article')
        assert check.text=='Create a new account', 'sign up page is broken'
        self.driver.find_element(By.XPATH, '//input[@placeholder="Pick a username (5 or more characters)"]').send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(4)

        #srp page
        check1=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[6]/button/span')
        assert check1.text=='Create secret recovery phrase for me', 'srp page is broken'
        self.driver.find_element(By.XPATH, '//button').click()
        time.sleep(3)

        #cp srp page
        check2=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/a/div/article')
        assert check2.text=="I'll do this later", 'copy srp page is broken'
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/a/div/article').click()
        time.sleep(2)

        #skip srp page
        check3=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[2]/article')
        assert check3.text=='Skip saving your secret recovery phrase?', 'Skipping srp page is broken'
        self.driver.find_element(By.XPATH, '//input').click()
        self.driver.find_element(By.XPATH, '//button[2]').click()
        time.sleep(10)

        #TOS page
        check4=self.driver.find_element(By.TAG_NAME, 'button')
        assert check4.text=='Create IOMe account', 'Tos page is broken'
        self.driver.find_element(By.XPATH, '//input').click()
        self.driver.find_element(By.XPATH, '//button').click()
        time.sleep(20)
