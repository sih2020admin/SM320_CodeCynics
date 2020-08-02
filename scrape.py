# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"


vesselname = input("Please enter name of the vessel: ")
vesselname = vesselname.upper()

driver = webdriver.Chrome(PATH)
driver.get("https://www.vesselfinder.com/vessels")


search = driver.find_element_by_id("advsearch-name")
search.clear()
search.send_keys(vesselname)
search.send_keys(Keys.RETURN)

try:
    resultslist = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, vesselname))
    )
    resultslist.click()

    information1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text2"))
    )
    information2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text1"))
    )

    info1=information1.text
    info2=information2.text

except:
    driver.close()
