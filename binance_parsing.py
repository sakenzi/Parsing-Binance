from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_driver)

driver.maximize_window()

driver.get('https://www.binance.com/ru/markets/overview?p=1')

driver.implicitly_wait(10)

title = driver.title
print(title)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, '//*[@id="tabContainer"]/div[3]/div[3]/div/div/div/div[2]/div[1]/div/a/div/div[1]/div[2]/div[1]')
#         )
#     )
#     print('Element:',element.list)
# except Exception as e:
#     print('Error', e)

#element = driver.find_element(By.XPATH, '//*[@id="tabContainer"]/div[3]/div[3]/div/div/div/div[2]/div[1]/div/a/div/div[1]/div[2]/div[1]')
element = driver.find_element(By.CSS_SELECTOR, '//*[@id="tabContainer"]/div[3]/div[3]/div/div/div/div[2]/div[1]/div/a/div/div[1]/div[2]/div[1]')
print(element)

current_url = driver.current_url
print(current_url)

driver.quit()