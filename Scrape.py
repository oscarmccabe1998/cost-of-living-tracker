from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def Scrape():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    targeturl = "https://www.gov.uk/national-minimum-wage-rates"
    browser.get(targeturl)

    soup = BeautifulSoup(browser.page_source, features='html.parser')

    rates = soup.find_all('tr')

    
    print(rates)

    browser.close()

if __name__ == "__main__":
    Scrape()