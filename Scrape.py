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

    rates = {}

    headings = soup.find_all('th')

    for row in rows:
        row_header = row.th.get_text()
        row_cell = row.td.get_text()
        rates[row_header] = row_cell

    #for row in rows:
    #    cols = row.find_all('td')
    #    cols = [ele.text.strip() for ele in cols]
    #    rates.append([ele for ele in cols if ele])
    
    #print(rows)
    print(rates)
    #print(headings)


    

if __name__ == "__main__":
    Scrape()
   # scheduler = BlockingScheduler()
   # scheduler.add_job(Scrape, 'interval', minutes = 1) #set to 1 minute for testing 
   # scheduler.start()