import time
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

price = 8500
seconds = time.time() + 3500

while price < 30000:
    ### WEB SCRAPPER ###
    # 1 ) Establishing connection to MangoDB
    client = MongoClient("mongodb+srv://Anis:Anis@mycluster-4apty.mongodb.net/<dbname>?retryWrites=true&w=majority")
    myDatabase = client["KijijiCars"]
    myUrlCollection = myDatabase["UrlCollection"]


    # 2) Establishing connection to Kijiji and setting up the environnement (150km)
    driver = webdriver.Chrome('/home/anis/Documents/Python/chromedriver.exe')
    driver.get("https://www.kijijiautos.ca/fr/voitures/#od=down&p={}:{}&sb=ct".format(price, price + 1500))
    driver.find_element_by_xpath("//button[@data-testid='LocationLabelLink']").click()
    driver.find_element_by_xpath("//select[@data-testid='LocationRadiusDropdown']").click()
    driver.find_element_by_xpath("//option[@value='150']").click()
    driver.find_element_by_xpath("//button[@data-testid='LocationModalSubmitButton']/span").click()

    #4) script will spend 25 minutes per URL
    while time.time() < seconds:
        # 4) Finding elements by xpath and extracting title, id and URL
        try:
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            liElements = driver.find_elements_by_xpath("//div[@data-testid='VehicleListItem']")
            for liElement in liElements:
                idElement = liElement.get_attribute("data-test-ad-id")
                linkElement = "https://www.kijijiautos.ca/fr/vip/{}/".format(idElement)
                
                # 4) if the id is not in the database, we insert it
                if myUrlCollection.find({"id":idElement}).count() == 0:
                    myUrlCollection.insert({"id":idElement, "title":"Car", "link":linkElement})
                    print("not in database")
                else:
                    print("in the list")
        except StaleElementReferenceException:
            print("problem")

    driver.close()
    price += 1500
    seconds = time.time() + 1800

