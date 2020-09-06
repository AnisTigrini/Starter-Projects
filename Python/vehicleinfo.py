import time
from selenium import webdriver
from pymongo import MongoClient


client = MongoClient("mongodb+srv://Anis:Anis@mycluster-4apty.mongodb.net/<dbname>?retryWrites=true&w=majority")
myDatabase = client["KijijiCars"]
myUrlCollection = myDatabase["UrlCollection"]
driver = webdriver.Chrome('/home/anis/Documents/Python/chromedriver.exe')

for link in myUrlCollection.find():
    driver.get(link["link"])
    time.sleep(2)
    caracterstics = dict()
    if len(driver.find_elements_by_xpath("//img[@alt='Non disponible']")) == 0:
        link.update()
        price = driver.find_element_by_xpath("//span[@data-testid='listing-basic-info-section-price']/span").get_attribute("innerHTML").replace("&nbsp","").replace(";","").replace("$","")
        print(price)
        vehcileDetails = driver.find_elements_by_xpath("//div[@data-testid='vehicleDetails']")
        
        for i in vehcileDetails[0].find_elements_by_tag_name("span"):
            print(i.get_attribute("innerHTML"))
    else:
        myUrlCollection.update_one({"id"},{"status":"inactive"})

driver.close()