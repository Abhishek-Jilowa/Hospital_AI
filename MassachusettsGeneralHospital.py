import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url_doctor = 'https://www.massgeneral.org'
chrome_driver_path = r"D:\Downlods(Original)\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)

# Function to scrape data from doctors profile
def scrape_section(soup,title):
    section = soup.find('p', class_='profile-detail__title', string=title)
    if section:
        list_items = section.find_next('div', class_='read-more__content').find_all('li')
        return [item.get_text(strip=True) for item in list_items]
    return []

#List to stoe doctors' info
doctors = []

#starting page of doctors list
startPage=1
#ending page of doctors list
endPage=60

for i in range(startPage,endPage+1):
    url='https://www.massgeneral.org/doctors?Text=*&Start='+str((i-1)*10+1)+'&MaxResults='+str(i*10)+'&Sort[]=lastname&MethodName=getlisting&PageNumber='+str(i)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    content_div = soup.find('div', class_='content')
    # Extract all anchor tags within the div
    driver.quit()
    if content_div:
        anchors = content_div.find_all('a')
        for anchor in anchors:
            href = anchor.get('href')  # Get the link (href attribute)
            text = anchor.text.strip()  # Get the text of the link
            if(href!="#"):
                url3=url_doctor+href
                driver1 = webdriver.Chrome(service=service)
                
                driver1.get(url3)
                time.sleep(3)

                html1 = driver1.page_source
                soup1 = BeautifulSoup(html1, 'html.parser')

                clinical_interests = scrape_section(soup1,"Clinical Interests:")
                treats = scrape_section(soup1,"Treats:")
                doctors.append({'Name': text,'Speciality':clinical_interests,'Treats':treats,'Hospital':"Massachusetts General Hospital",'Profile':url3})
                driver1.quit()
    else:
        print("Div with class 'content' not found.")
    

df = pd.DataFrame(doctors)
df.to_csv('doctors_data.csv', index=False) 