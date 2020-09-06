import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/home/anis/Documents/Python/chromedriver')
driver.get("https://www.autotrader.ca/cars/qc/montr%c3%a9al/?rcp=0&rcs=0&prx=100&prv=Quebec&loc=H1Y%203K9&hprc=True&wcp=True&sts=New-Used&inMarket=basicSearch")
driver.find_element_by_id("btnGotIt").click()
time.sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
a = driver.find_elements_by_class_name("result-item")
print(len(a))
time.sleep(100)
driver.close()
