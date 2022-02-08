from selenium import webdriver
from bs4 import BeautifulSoup

def Scrape():
    browser = webdriver.Firefox()
    targeturl = "https://www.deliveringforscotland.gov.uk/at-work/nlw-nmw/"
    browser.get(targeturl)

    soup = BeautifulSoup(browser.page_source, features='html.parser')

    print(soup.prettify())

    browser.close()

if __name__ == "__main__":
    Scrape()