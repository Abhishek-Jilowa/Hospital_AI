from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome()

url = 'https://www.uclahealth.org/providers/search' 
driver.get(url)
time.sleep(3)
Doctors=[]
i=0
while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    parent_div = soup.find('div', class_='space-y-6 mt-6')
    # Find all nested divs that contain the 'about' attribute
    nested_divs = parent_div.find_all('div', attrs={'about': True})
    # Loop through and extract the 'about' attributes
    for div in nested_divs:
        about_url = div['about']
        base_url="https://www.uclahealth.org"
        # driver1 = webdriver.Chrome(service=service)
        driver1 = webdriver.Chrome()
        driver1.get(base_url+about_url)
        time.sleep(3)
        page_source1= driver1.page_source
        soup1 = BeautifulSoup(page_source1, 'html.parser')
        name = soup1.find(itemprop="name").text
        # Extract department
        department = soup1.find(itemprop="MedicalSpecialty").text
        Doctors.append({'Name': name,'Departments':department,'Hospital':"UCLA Health - Ronald Reagan Medical Center",'Profile':base_url    +about_url})
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '.flex .items-center')
        next_button.click()
        time.sleep(3)
    
    except Exception as e:
        # print("No more pages to scrape or error occurred:", e)
        break


driver.quit()
df = pd.DataFrame(Doctors)
df.to_csv('UCLA.csv', index=False)