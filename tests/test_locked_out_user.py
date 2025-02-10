import time
from selenium.webdriver.common.by import By


def test_locked_out_user(setup_browser):
    """Test locked_out_user login and verify error message."""
    driver = setup_browser
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Sorry, this user has been locked out." in error_msg
    print("✅ Locked-out user test passed.")
