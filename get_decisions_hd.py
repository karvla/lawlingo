import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import urllib.request
import regex as re

BASE_URL = "https://www.domstol.se/"

# TODO: Fix duplication-bug
def print_urls():
    url = "https://www.domstol.se/hogsta-domstolen/avgoranden/?f=DecisionType_list:decision"
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    banner_button = driver.find_element_by_class_name("banner__button")
    more_button = driver.find_element_by_class_name("search-result-item__show-more-btn")

    banner_button.click()
    for i in range(100):
        more_button.click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-result-item__show-more-btn')))
        results = driver.find_elements_by_class_name("u-pr-huge--large")[i*19:]
        for item in results:
            url = item.get_attribute("href")
            print(url)

def download_pdfs(url_path):
    with open(url_path) as f:
        urls = f.read().splitlines()

    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        pdf_element = soup.find("a", href=re.compile(r".+\.pdf"))
        if pdf_element is not None:
            pdf_url = BASE_URL + pdf_element["href"]
            file_name = re.findall(r"(.+\/)*(.+\..+)$", pdf_url)[0][1]
            urllib.request.urlretrieve(pdf_url, "./" + file_name)
            print("Downloaded:", file_name)
        else:
            print("Skipped one")

if __name__ == '__main__':
    download_pdfs('./links.txt')
    



