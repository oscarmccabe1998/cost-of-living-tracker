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

    rows = soup.find_all('tr')
    payrates = soup.find_all('td')

    headings = []
    tablerow = []
    contents = []

    rates = {}
    for x in range(len(payrates)):

        headings.append(soup.find_all('td')[x].contents)

    for row in range(len(rows)):
        tablerow.append(soup.find_all('th')[row].contents)
        contents.append(soup.find_all('td')[row].contents)

    
    print(tablerow)
    print(headings)
    print(len(soup.find_all('table')))

    class minWage:
        def __init__(self, years, ageBracket, hourlyRate):
            self.years = years
            self.ageBracket = ageBracket
            self.hourlyRate = hourlyRate

        def printclass(self):
            print("data inside the class is " + self.years + self.ageBracket + self.hourlyRate)
    

if __name__ == "__main__":
   # Scrape()
    scheduler = BlockingScheduler()
    scheduler.add_job(Scrape, 'interval', minutes = 1) #set to 1 minute for testing 
    scheduler.start()