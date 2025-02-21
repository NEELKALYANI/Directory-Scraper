from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.gallup.com/learning/certification/en/directory"
driver.get(url)
time.sleep(3)

data = []

for index in range(1, len(Select(driver.find_element(By.XPATH, "/html/body/div[2]/div/form/main/article/div[2]/div/div/div[1]/div[1]/div/select")).options)):
    dropdown = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/main/article/div[2]/div/div/div[1]/div[1]/div/select")
    select = Select(dropdown)
    option = select.options[index]
    country_name = option.text
    print(f"Scraping data for: {country_name}")

    select.select_by_visible_text(country_name)

    apply_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/main/article/div[2]/div/div/div[1]/div[4]/input")
    apply_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "c-tile--coach"))
    )

    people = driver.find_elements(By.CLASS_NAME, "c-tile--coach")

    for person in people:
        try:
            name_element = person.find_element(By.TAG_NAME, "h4")
            name = name_element.text.strip() if name_element else "N/A"
        except:
            name = "N/A"

        try:
            email_element = person.find_element(By.TAG_NAME, "a")
            email = email_element.text.strip() if email_element else "N/A"
        except:
            email = "N/A"
        
        try:
            image_element = person.find_element(By.TAG_NAME, "img")
            image_src = image_element.get_attribute("src") if image_element else "N/A"
        except:
            image_src = "N/A"

        data.append([country_name, name, email, image_src])

df = pd.DataFrame(data, columns=["Country", "Name", "Email", "Image"])
df.to_excel("scraped_data.xlsx", index=False)

print("Data saved to scraped_data.xlsx")

driver.quit()