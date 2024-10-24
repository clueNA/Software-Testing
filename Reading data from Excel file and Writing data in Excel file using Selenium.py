from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import io
import os


def capture_partial_screenshot(driver, element, save_path):
    # Capture the full page screenshot as PNG
    screenshot = driver.get_screenshot_as_png()

    # Convert the screenshot to a PIL Image
    screenshot_image = Image.open(io.BytesIO(screenshot))

    # Get the element's location and size
    location = element.location
    size = element.size

    # Define the bounding box for the element
    left = 100
    top = 400
    right = left + size['width']
    bottom = top + size['height']

    # Crop the screenshot to the bounding box of the element
    element_screenshot = screenshot_image.crop((left, top, right, bottom))

    # Save the cropped screenshot
    element_screenshot.save(save_path)
    print(f"Partial screenshot saved at {save_path}")


if _name_ == "_main_":
    # Set up the driver (ensure you have the correct path to your chromedriver)
    driver = webdriver.Chrome()

    # Navigate to the desired URL
    driver.get("https://www.google.com")

    # Locate the element (e.g., Google's search box)
    element = driver.find_element(By.NAME, "q")

    # Define the path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "partial_screenshot.png")

    # Capture and save the partial screenshot
    capture_partial_screenshot(driver, element, downloads_path)

    # Quit the driver
    driver.quit()