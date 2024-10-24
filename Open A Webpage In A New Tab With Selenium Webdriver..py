from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def open_new_tab(driver, url):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)

driver = webdriver.Chrome()

try:
    # Navigate to an initial page
    initial_url = "https://kayoanime.com/"
    driver.get(initial_url)
    print(f"Opened initial page: {initial_url}")

    # Open a new tab and navigate to a different page
    new_url = "https://hianime.nz/home"
    open_new_tab(driver, new_url)
    print(f"Opened new tab with: {new_url}")

    # Wait for an element on the new page to ensure it's loaded
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit"))
        )
        print("New page loaded successfully")
    except TimeoutException:
        print("Timed out waiting for page to load")

    # Demonstrate switching back to the original tab
    driver.switch_to.window(driver.window_handles[0])
    print(f"Switched back to the original tab: {driver.current_url}")

    # Wait for user input before closing
    input("Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed")