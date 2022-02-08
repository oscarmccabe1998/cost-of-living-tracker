from selenium import webdriver
from bs4 import BeautifulSoup

def Scrape():
    browser = webdriver.Firefox()
    targeturl = "https://www.gov.uk/national-minimum-wage-rates"
    browser.get(targeturl)

    soup = BeautifulSoup(browser.page_source, features='html.parser')

    rates = soup.find_all('tr')

    #print(soup.prettify())
    print(rates)

    browser.close()

if __name__ == "__main__":
    Scrape()