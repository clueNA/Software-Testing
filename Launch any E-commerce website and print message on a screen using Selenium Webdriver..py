from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

# Start a WebDriver session (assuming Chrome driver here)
driver = webdriver.Chrome()

# Navigate to Amazon.com
driver.get("https://www.amazon.com/")

# Show an alert message when the website is opened
alert = Alert(driver)
alert_text = "Amazon website opened successfully!"
driver.execute_script(f"alert('{alert_text}');")

# Wait for a few seconds to see the alert
time.sleep(5)

# Accept the alert
alert.accept()

# Print a message indicating the action taken
print("Navigated to the first product page.")

# Close the WebDriver session
driver.quit()