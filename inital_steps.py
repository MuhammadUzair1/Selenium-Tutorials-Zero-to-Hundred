from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'http://adamchoi.co.uk/leagues/spain-la-liga'
path = r'C:\Selenium Drivers\chromedriver-win64\chromedriver.exe'
service = Service(path)
service.start()

driver = webdriver.Chrome(path)
driver.get(website)

driver.find_element_by_xpath("//a[@data-ng-click=\"vm.setTabType('League Table & Team Averages')\"]").click()

