from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Setup the WebDriver (Chrome in this example)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the website
    print("Navigating to the website...")
    driver.get("https://the-internet.herokuapp.com")
    print("Page loaded.")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Initialize ActionChains
    actions = ActionChains(driver)
# Example 1: Hover over an element
    print("Attempting to hover over an element...")
    try:
        driver.get("https://the-internet.herokuapp.com/hovers")
        hover_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "figure"))
        )
        actions.move_to_element(hover_element).perform()
        print("Hover action completed.")
    except TimeoutException:
        print("Hover element not found within timeout period.")
    except Exception as e:
        print(f"An error occurred during hover action: {e}")
# Example 2: Drag and Drop
    print("Attempting drag and drop...")
    try:
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        source = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "column-a"))
        )
        target = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "column-b"))
        )
        actions.drag_and_drop(source, target).perform()
        print("Drag and drop completed.")
    except TimeoutException:
        print("Drag and drop elements not found within timeout period.")
    except Exception as e:
        print(f"An error occurred during drag and drop: {e}")

    # Example 3: Key Actions
    print("Attempting key actions...")
    try:
        driver.get("https://the-internet.herokuapp.com/key_presses")
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        input_field.send_keys(Keys.ENTER)
        print("Enter key pressed.")
    except TimeoutException:
        print("Input field not found within timeout period.")
    except Exception as e:
        print(f"An error occurred during key actions: {e}")
    # Example 4: Context Click (Right Click)
    print("Attempting context click...")
    try:
        driver.get("https://the-internet.herokuapp.com/context_menu")
        context_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hot-spot"))
        )
        actions.context_click(context_element).perform()
        print("Context click completed.")
    except TimeoutException:
        print("Context element not found within timeout period.")
    except Exception as e:
        print(f"An error occurred during context click: {e}")
        
    print("All actions attempted. The browser will remain open for 30 seconds.")
    time.sleep(30)

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Closing the browser...")
    driver.quit()