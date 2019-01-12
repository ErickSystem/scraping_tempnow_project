import os
import re
import time

from datetime import datetime
from common.dao import querys
from common.datasource import connection
from common import util
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from lib_formatter_logger import log

logger = log.getLogger('tempnow')

DRIVE_CHROME = os.getcwd() + '/drives/chromedriver'
URL = 'https://www.tempoagora.com.br'
URL_STATE = f'{URL}/previsao-do-tempo'

def mount_links():
    '''

    '''
    links = list()
    brasil = 1
    count = 0

    for state in querys.get_all_regions(brasil):
        for city in querys.consult_locality_byregionid(state['id']):
            data = dict()
            # The code below serves to limit the total number of cities that will be consulted.
            if count > 1:
                break

            data['link'] = URL_STATE + '/{0}/{1}'.format(state['code'], util.format_cityname(city['name']))
            data['locality_id'] = city['id']
            links.append(data)

            count += 1
        count = 0

    return links

def weather_day(bs4, locality_id, date_time):
    '''

    '''
    parameters = dict()
    lag = querys.consult_lag(locality_id)
    if lag:
        lag = max([l['lag'] for l in lag], key=int)
        lag += 1
        parameters['lag'] = lag
    else:
        parameters['lag'] = 0
    
    _max = bs4.find_all("span", class_="weather-info-vert--max-temp", limit=1)[0].text
    _max = _max.replace(" ", "")
    _max = _max.replace("\n", "")
    _min = bs4.find_all("span", class_="weather-info-vert--min-temp", limit=1)[0].text
    _min = _min.replace(" ", "")
    _min = _min.replace("\n", "")

    precipitation = bs4.find_all("span", class_="weather-info-vert--precipitation", limit=1)[0].text
    precipitation = precipitation.replace("\n", "")
    precipitation = precipitation.strip(' ')
    precipitation = precipitation.split(' ')[0]
    parameters['max'] = util.convert_by_int(_max[:2])
    parameters['min'] = util.convert_by_int(_min[:2])
    parameters['precipitation'] = util.convert_by_int(precipitation)
    parameters['date'] = date_time.date()
    parameters['locality_id'] = locality_id
    
    weather = bs4.find_all("span", class_="weather-info-vert--climate-icon", limit=1)[0]
    parameters['weather'] = weather.get('title')

    trans, conn = connection.return_conn_tran()
    if querys.create_wfday(parameters=parameters, conn=conn):
        trans.commit()
        conn.close()
    else:
        trans.rollback()
        conn.close()    

def weather_hour(bs4, locality_id, date_time):
    '''

    '''
    parameters = dict()
    parameters['locality_id'] = locality_id
    parameters['date_time'] = date_time
    tmp = bs4.find_all("span", class_="weather-temperature--temperature")[0].text[:2] # ex: change of 24 ° to 24 only
    parameters['temp'] = util.convert_by_int(tmp)  
    parameters['weather'] = bs4.find_all("div", class_="weather-icon")[0].get('title')

    last_update = bs4.find_all("div", class_="info__updated-at")[0].text
    last_update = last_update.replace("\n", "")
    parameters['last_update'] = last_update.strip(" ")
        
    bs4_hour = bs4.find_all("ul")[1]
    bs4_hour = bs4_hour.find_all("li")
    for l in bs4_hour:
        if l.get('title') == 'Velocidade do vento':
            wind = l.text
            wind = wind.split(' ')[0]
            parameters['wind'] = util.convert_by_int(wind)
        elif l.get('title') == 'Pressão atmosférica':
            atmospheric_pressure = l.text
            atmospheric_pressure = atmospheric_pressure.split(' ')[0]
            parameters['atmospheric_pressure'] = util.convert_by_int(atmospheric_pressure)
        elif l.get('title') == 'Umidade relativa':
            relative_humidity = l.text
            relative_humidity = relative_humidity.split(' ')[0]
            parameters['relative_humidity'] = util.convert_by_int(relative_humidity[:2])

    trans, conn = connection.return_conn_tran()
    if querys.create_wfhour(parameters=parameters, conn=conn):
        trans.commit()
        conn.close()
    else:
        trans.rollback()
        conn.close()

def scraping_data(date_time):
    '''

    '''
    # load drive
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(
            executable_path=DRIVE_CHROME, 
            desired_capabilities=capa
    )
    for link in mount_links():
        try:
            driver.get(link['link'])
            wait = WebDriverWait(driver, 20)
            temp_day = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div')))
            temp_hour = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[1]/header/div[1]')))
        except TimeoutException:
            logger.exception('not found element page [{0}]'.format(link['link']))
            continue
        except Exception as e:
            logger.exception('unexpected error [{0}]'.format(e))
            continue
        
        try:
            # EXEC TO HOUR
            temp_hour_html = temp_hour.get_attribute('innerHTML')
            weather_hour(bs(temp_hour_html, 'html.parser'), link['locality_id'], date_time)
            # EXEC TO DAY
            temp_day_html = temp_day.get_attribute('innerHTML')
            weather_day(bs(temp_day_html, 'html.parser'), link['locality_id'], date_time)
        except Exception as e:
            logger.exception('unexpected error [{0}]'.format(e))
            continue

    driver.quit()

def main():
    '''
        function main
    '''
    now = datetime.now()
    now = now.replace(minute=0, second=0, microsecond=0)
    scraping_data(now)

if __name__ == '__main__':
    main()