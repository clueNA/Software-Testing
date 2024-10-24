from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Handling Drop-down
def handle_dropdown():
    try:
        # Open the target web page
        driver.get('https://www.amazon.in/Yakuza-Blue-Electric-Scooty-Lead/dp/B0CNRYQ9BK')
        dropdown = Select(driver.find_element('id', 'searchDropdownBox'))
        dropdown.select_by_visible_text('Gift Cards')  # Change 'Gift Cards' to the actual text of the dropdown option
        print("Dropdown handled successfully.")
    except Exception as e:
        print(f"Error handling dropdown: {e}")

# Handling File Upload
def handle_file_upload():
    try:
        driver.get('https://www.w3schools.com/howto/howto_html_file_upload_button.asp')
        file_input = driver.find_element('id', 'myFile')
        file_input.send_keys('report.md')  # Change to your file path
        # Optionally click the submit button if needed
        # driver.find_element('xpath', '//input[@type="submit"]').click()
        print("File upload handled successfully.")
    except Exception as e:
        print(f"Error handling file upload: {e}")

# Handling Alerts
def handle_alert():
    try:
        driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
        driver.switch_to.frame("iframeResult")
        driver.find_element('xpath', '//button[contains(text(),"Try it")]').click()
        alert = driver.switch_to.alert
        time.sleep(3)
        alert.accept()
        driver.switch_to.default_content()
        print("Alert handled successfully.")
    except Exception as e:
        print(f"Error handling alert: {e}")

# Handling Pop-ups
def handle_popups():
    try:
        driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open')
        driver.switch_to.frame("iframeResult")
        driver.find_element('xpath', '//button[contains(text(),"Try it")]').click()
        main_window = driver.current_window_handle
        all_windows = driver.window_handles
        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                break
        # Perform actions in the new window
        time.sleep(5)  # Just to keep the new window open for a while
        driver.close()
        driver.switch_to.window(main_window)
        print("Pop-up handled successfully.")
    except Exception as e:
        print(f"Error handling popups: {e}")

# Run the handlers one by one
handle_dropdown()
time.sleep(5)  # Pause to see the result

handle_file_upload()
time.sleep(5)  # Pause to see the result

handle_alert()
time.sleep(5)  # Pause to see the result

handle_popups()
time.sleep(5)  # Pause to see the result

# Close the browser
driver.quit()