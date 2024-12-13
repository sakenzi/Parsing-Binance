from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from models.parser_models import EntityCrypto, AttributeCrypto, ValuesCrypto
from models.settings import session


chrome_driver = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_driver)
driver.maximize_window()

def get_or_create_attribute(session, attribute_name):
    attribute = session.query(AttributeCrypto).filter_by(name_attribute=attribute_name).first()
    if not attribute:
        attribute = AttributeCrypto(name_attribute=attribute_name)
        session.add(attribute)
        session.commit()
    return attribute.id

def procces_page(driver):
    try:
        for i in range(1, 31):
            if i <= 8:
                short_name_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/a/div/div/div[2]/div[1]'
                short_name_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, short_name_xpath))
                )
                full_name_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/a/div/div/div[2]/div[2]'
                full_name_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, full_name_xpath))
                )
                price_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div[1]'
                price_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, price_xpath))
                )
                percentage_change_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div[2]'
                percentage_change_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, percentage_change_xpath))
                )
                volume_for_the_period_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div[3]'
                volume_for_the_period_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, volume_for_the_period_xpath))
                )
                capitalization_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div[4]'
                capitalization_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, capitalization_xpath))
                )

                entity = session.query(EntityCrypto).filter_by(short_name=short_name_element.text).first()
                if not entity:
                    entity = EntityCrypto(short_name=short_name_element.text, full_name=full_name_element.text)
                    session.add(entity)
                    session.commit()

                attributes = {
                    "price": price_element.text,
                    "percentage_change": percentage_change_element.text,
                    "volume_for_the_period": volume_for_the_period_element.text,
                    "capitalization": capitalization_element.text,
                }

                for attr_name, attr_value in attributes.items():
                    attr_id = get_or_create_attribute(session, attr_name)
                    value_entry = ValuesCrypto(
                        values=attr_value,
                        entity_id=entity.id,
                        attribute_id=attr_id
                    )
                    session.add(value_entry)

                session.commit()

                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", short_name_element)

            else:
                short_name_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/a/div/div/div[2]/div[1]'
                short_name_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, short_name_xpath))
                )
                full_name_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/a/div/div/div[2]/div[2]'
                full_name_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, full_name_xpath))
                )
                price_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/div[1]'
                price_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, price_xpath))
                )
                percentage_change_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/div[2]'
                percentage_change_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, percentage_change_xpath))
                )
                volume_for_the_period_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/div[3]'
                volume_for_the_period_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, volume_for_the_period_xpath))
                )
                capitalization_xpath = f'/html/body/div[3]/div/div/div/main/div/div[3]/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div[{i}]/div/div/div[4]'
                capitalization_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, capitalization_xpath))
                )

                entity = session.query(EntityCrypto).filter_by(short_name=short_name_element.text).first()
                if not entity:
                    entity = EntityCrypto(short_name=short_name_element.text, full_name=full_name_element.text)
                    session.add(entity)
                    session.commit()

                attributes = {
                    "price": price_element.text,
                    "percentage_change": percentage_change_element.text,
                    "volume_for_the_period": volume_for_the_period_element.text,
                    "capitalization": capitalization_element.text,
                }

                for attr_name, attr_value in attributes.items():
                    attr_id = get_or_create_attribute(session, attr_name)
                    value_entry = ValuesCrypto(
                        values=attr_value,
                        entity_id=entity.id,
                        attribute_id=attr_id
                    )
                    session.add(value_entry)

                session.commit()

                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", short_name_element)

    except Exception as e:
        print(f'Error on current page: {e}')


def go_to_page(driver, page_number):
    current_url = driver.current_url
    new_url = current_url.split('?')[0] + f"?p={page_number}"
    driver.get(new_url)


try:
    driver.get('https://www.binance.com/ru/markets/overview?p=1')
    total_pages = 13  
    for page in range(1, total_pages + 1):
        print(f'Парсинг страницы {page}')
        procces_page(driver)  
        if page < total_pages:
            go_to_page(driver, page + 1)  
            time.sleep(3)  

except Exception as e:
    print(f'Global Error: {e}')

finally:
    driver.quit()
    session.close()


#timescale
#clickhouse
#уровни http и https
#eav