from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import time

URL = "https://www.demoblaze.com/index.html"

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
service = Service("chromedriver")  # Update with correct path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Scrape laptop data
def scrape_laptops():
    laptops = []
    driver.get(URL)
    time.sleep(3)  # Allow time for JavaScript to load

    while True:
        items = driver.find_elements(By.CLASS_NAME, "card-block")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "card-title").text
            price = item.find_element(By.TAG_NAME, "h5").text
            description = item.find_element(By.CLASS_NAME, "card-text").text
            
            laptops.append({
                "name": name,
                "price": price,
                "description": description
            })

        # Check for "Next" button and click it
        try:
            next_button = driver.find_element(By.ID, "next2")
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(2)  # Wait for next page to load
        except:
            break  # Exit loop if "Next" button is not found

    return laptops

# Save data to JSON
def save_to_json(data, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    laptops = scrape_laptops()
    save_to_json(laptops)
    driver.quit()  # Close browser
    print("Laptop listings scraped and saved.")
