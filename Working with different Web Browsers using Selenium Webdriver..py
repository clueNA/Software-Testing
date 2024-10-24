from selenium import webdriver


# Open Chrome browser
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://kayoanime.com/")

# Open Safari browser (on MacOS)
driver = webdriver.Edge()
driver.get("https://kayoanime.com/")

# Close the browser
driver.quit()