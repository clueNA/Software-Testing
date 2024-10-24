from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://www.w3schools.com/')

# Wait for the page to load completely
time.sleep(3)

# Refresh the webpage
driver.refresh()

# Alternatively, you can use JavaScript to refresh the page
driver.execute_script("location.reload()")

# Wait for the page to load completely after refresh
time.sleep(3)

# Close the browser
driver.quit()