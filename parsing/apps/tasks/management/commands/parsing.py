from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from django.db import transaction
import time
from apps.tasks.models import EntityCrypto, ValuesCrypto, AttributeCrypto
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
from apps.tasks.models import ParsingSettings


def handle():
    print(f"Парсинг начался: {datetime.now()}")
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    def get_or_create_attribute(attribute_name):
        attribute, created = AttributeCrypto.objects.get_or_create(name_attribute=attribute_name)
        return attribute

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

                    with transaction.atomic():
                        entity, created= EntityCrypto.objects.get_or_create(
                            short_name=short_name_element.text,
                            full_name = full_name_element.text
                        )

                        attributes = {
                            'price': price_element.text,
                            "percentage_change": percentage_change_element.text,
                            "volume_for_the_period": volume_for_the_period_element.text,
                            "capitalization": capitalization_element.text,
                        }

                        for attr_name, attr_value in attributes.items():
                            if attr_value is not None:
                                attribute = get_or_create_attribute(attr_name)
                                ValuesCrypto.objects.create(
                                    values=attr_value,
                                    entity=entity,
                                    attributes=attribute
                                )
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", short_name_element)

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

                    with transaction.atomic():
                        entity, created= EntityCrypto.objects.get_or_create(
                            short_name=short_name_element.text,
                            full_name = full_name_element.text
                        )

                        attributes = {
                            'price': price_element.text,
                            "percentage_change": percentage_change_element.text,
                            "volume_for_the_period": volume_for_the_period_element.text,
                            "capitalization": capitalization_element.text,
                        }

                        for attr_name, attr_value in attributes.items():
                            if attr_value is not None:
                                attribute = get_or_create_attribute(attr_name)
                                ValuesCrypto.objects.create(
                                    values=attr_value,
                                    entity=entity,
                                    attributes=attribute
                                )
                            
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", short_name_element)

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

def start():
    print("Запуск планировщика ...")
    scheduler = BackgroundScheduler()
    try:
        parsing_settings = ParsingSettings.objects.first()
        if parsing_settings:
            interval_minutes = parsing_settings.interval_minutes
        else:
            interval_minutes = 10
            print('Настройки не найдены. Используется значение по умолчанию: 10 минут.')
        
        scheduler.add_job(
            handle,
            'interval',
            minutes = interval_minutes,
            max_instances=1,
            coalesce=False
        )

        scheduler.start()
        print(f"Планировщик запущен с интервалом: {interval_minutes} минут.")
    except Exception as e:
        print(f"Ошибка при запуске планировщика: {e}")