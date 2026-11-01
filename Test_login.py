import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demowebshop.tricentis.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


class TestLogin:
    def test_login_success(self, driver):
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("QA54_Helen@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("QA54_Helen")
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

        logout = driver.find_element(By.CSS_SELECTOR, "a.ico-logout")
        assert logout.is_displayed()


