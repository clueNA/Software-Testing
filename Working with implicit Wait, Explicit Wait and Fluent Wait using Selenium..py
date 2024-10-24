from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def implicit_wait_example(driver):
   
    driver.implicitly_wait(10)
    driver.get("https://www.zomato.com/")
    print("Current URL (Implicit Wait):", driver.current_url)
    try:
        element = driver.find_element(By.NAME, "Store")  
        print("Element found using implicit wait")
    except :
        print("Element not found using implicit wait")

def explicit_wait_example(driver):
    driver.get("https://www.zomato.com/")
    print("Current URL (Explicit Wait):", driver.current_url)
    try:
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Gmail")) 
        )
        print("Element found using explicit wait")
    except Exception as e:
        print("Element not found using explicit wait:", e)

def fluent_wait_example(driver):
    driver.get("https://www.zomato.com/")
    print("Current URL (Fluent Wait):", driver.current_url)
    try:
        
        fluent_wait = WebDriverWait(driver, 10, poll_frequency=1)
        element = fluent_wait.until(
            EC.presence_of_element_located((By.NAME, "Images")) 
        )
        print("Element found using fluent wait")
    except Exception as e:
        print("Element not found using fluent wait:", e)

if __name__ == "_main_":

    driver = webdriver.Chrome()

    implicit_wait_example(driver)
    explicit_wait_example(driver)
    fluent_wait_example(driver)

    driver.quit()