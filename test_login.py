import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Products']"))
    )
    page_menu = driver.find_element(By.XPATH, "//span[text()='Products']").text
    assert page_menu == "Products"
    driver.quit()