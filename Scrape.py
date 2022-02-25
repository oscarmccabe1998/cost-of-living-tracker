from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

def Scrape():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    targeturl = "https://www.gov.uk/national-minimum-wage-rates"
    browser.get(targeturl)

    soup = BeautifulSoup(browser.page_source, features='html.parser')

    browser.close()

    rates = soup.find_all('tr')

    
    print(rates)


    

if __name__ == "__main__":
    #Scrape()
    scheduler = BlockingScheduler()
    scheduler.add_job(Scrape, 'interval', minutes = 1) #set to 1 minute for testing 
    scheduler.start()