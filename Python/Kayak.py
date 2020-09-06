from selenium import webdriver
import time
import datetime


driver = webdriver.Chrome('/home/anis/Documents/Python/chromedriver.exe')
driver.get('https://www.ca.kayak.com/flights/YMQ-LON/2020-09-01/2020-09-10?sort=price_a')
time.sleep(10)
b = driver.find_elements_by_class_name("Base-Results-HorizonResult")

for i in range(0, 4):
    print(b[i].get_attribute('aria-label'))

time.sleep(900)
driver.close()

print(datetime.datetime(year=2020, month=1, day=31) - datetime.datetime.now())

now = datetime.datetime.now()
