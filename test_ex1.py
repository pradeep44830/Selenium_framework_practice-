import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_ex1():
    chrome_options = Options()

    # Disabling password manager popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    header = driver.find_element(By.CLASS_NAME,"login_logo").text
    assert header == "Swag Labs"
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)
    page_menu = driver.find_element(By.CLASS_NAME, "title").text
    assert page_menu == "Products"
    driver.quit()