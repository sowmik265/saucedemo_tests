import time
from selenium.webdriver.common.by import By
from conftest import login


def reset_app(driver):
    """Reset application state."""
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "reset_sidebar_link").click()
    time.sleep(1)


def logout(driver):
    """Logout user."""
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)


def checkout(driver):
    """Proceed to checkout."""
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    driver.find_element(By.ID, "first-name").send_keys("Tanvir")
    driver.find_element(By.ID, "last-name").send_keys("Ahamed")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)
    success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_msg == "Thank you for your order!"


def test_standard_user_checkout(setup_browser):
    """Test standard_user checkout process."""
    driver = setup_browser
    login(driver, "standard_user", "secret_sauce")
    reset_app(driver)

    # Add 3 items to cart
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")[:3]
    total_price = 0.0
    for item in items:
        price = float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", ""))
        total_price += price
        item.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)

    # Go to cart and verify items
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    checkout(driver)
    print("✅ Standard user checkout test passed.")

    reset_app(driver)
    logout(driver)
