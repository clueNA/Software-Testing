from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org")

search_input = driver.find_element(By.ID, "searchInput")
search_input.send_keys("Python programming")
search_input.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstHeading")))

page_title = driver.execute_script("return document.title;")
print(f"Page title: {page_title}")

first_paragraph = driver.execute_script("""
    var paragraphs = document.getElementsByTagName('p');
    for (var i = 0; i < paragraphs.length; i++) {
        if (paragraphs[i].textContent.trim().length > 0) {
            return paragraphs[i].textContent.trim();
        }
    }
    return '';
""")
print(f"First paragraph: {first_paragraph}")

# Get all external links in the article
external_links = driver.execute_script("""
    var links = document.querySelectorAll('a.external');
    return Array.from(links).map(link => link.href);
""")
print("External links:")
for link in external_links[:5]:  
    print(link)

driver.quit()