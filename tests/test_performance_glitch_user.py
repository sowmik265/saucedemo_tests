import time
from selenium.webdriver.common.by import By
from conftest import login


def test_performance_glitch_user(setup_browser):
    """Test performance_glitch_user checkout."""
    driver = setup_browser
    login(driver, "performance_glitch_user", "secret_sauce")

    # Sort items Z → A
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.XPATH, "//option[@value='za']").click()
    time.sleep(2)

    # Add first item to cart
    item = driver.find_element(By.CLASS_NAME, "inventory_item")
    name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    item.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    # Go to cart and verify
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item_name == name

    # Proceed to checkout
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

    print("✅ Performance glitch user checkout test passed.")
