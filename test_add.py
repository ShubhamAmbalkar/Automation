# Swag Demo TEST
# testing
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def test_setup():
    global driver
    driver.implicitly_wait(10)
    driver = webdriver.Chrome()
    driver.maximize_window()


def test_validLogin(test_setup):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    if driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').is_displayed():
        assert True
    else:
        assert False
    driver.close()


def test_invalidLogin(test_setup):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_auce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    if driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]').is_displayed():
        driver.save_screenshot('C://Users//Austin//PycharmProjects//Python//InvalidLogin.png')
        assert True
    else:
        assert False
    driver.close()


def test_addtocart(test_setup):
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    if driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').is_displayed():
        driver.save_screenshot('C://Users//Austin//PycharmProjects//Python//Add_To_Cart.png')
        assert True
    else:
        assert False
    driver.close()
