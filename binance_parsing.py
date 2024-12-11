from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_driver)

driver.maximize_window()

driver.get('https://www.binance.com/ru/markets/overview?p=1')

driver.implicitly_wait(10)

title = driver.title
print(title)

def procces_page(driver, page_number):
    try:
        for i in range(1, 31):
            if i <= 8:
                first_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/a/div/div/div[2]/div[1]'
                first_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, first_xpath))
                )
                print(f'{i}_Element:{first_element.text}')
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", first_element)
            else:
                first_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/a/div/div/div[2]/div[1]'
                first_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, first_xpath))
                )
                print(f'{i} Element:{first_element.text}')
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", first_element)

    except Exception as e:
        print(f'Error: {e}')

def go_to_page(driver, page_number):
    current_url = driver.current_url
    new_url = current_url.split('?')[0] + f"?p={page_number}"
    driver.get(new_url)

try:
    driver.get('https://www.binance.com/ru/markets/overview?p=1')
    total_pages = 14
    for page in range(1, total_pages):
        procces_page(driver, page)
        if page < total_pages:
            go_to_page(driver, page + 1)

except Exception as e:
        print(f'Error: {e}')

finally:
    driver.quit()