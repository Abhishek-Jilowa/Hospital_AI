from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver1 = webdriver.Chrome()

driver1.get("https://my.clevelandclinic.org/departments")

# Set up WebDriverWait
wait = WebDriverWait(driver1, 10)

page_source1 = driver1.page_source
soup1 = BeautifulSoup(page_source1, 'html.parser')

anchor_tags = soup1.find_all('a', class_='index-list-link')
Doctors = []
driver1.quit()

for anchor in anchor_tags:
    if(len(Doctors)>1000):
        break
    driver = webdriver.Chrome()
    url="https://my.clevelandclinic.org"
    href = anchor.get('href')  # Get the href attribute
    url_to_docs=url+href+"/staff"


    driver.get(url_to_docs)

    # Set up WebDriverWait
    wait = WebDriverWait(driver, 10)

    # Loop to click the "Load More" button multiple times
    while True:
        try:
            # Find the "Load More" button by class name and click it
            load_more_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'js-go-to-page')))
            load_more_button.click()

            # Wait for new content to load (adjust time as needed)
            time.sleep(3)

        except Exception as e:
            break

    # After all content is loaded, get the page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page
    soup = BeautifulSoup(page_source, 'html.parser')


    doctors = soup.find_all('div', class_='provider-search__result-wrapper')

# Loop through each doctor profile container
    for doctor in doctors:
        # Extract the doctor's name and link to the profile
        name_tag = doctor.find('a', href=True)
        name = name_tag.get_text(strip=True)
        profile_link = name_tag['href']

        # Extract the departments (only from the "Departments" section)
        department_section = doctor.find('h3', string="Departments")

        if department_section:
            # Look for the corresponding <ul> right after the "Departments" heading
            departments_ul = department_section.find_next('ul')

            # Explicitly extract text from each <li> and ensure no tags are included
            departments_list = departments_ul.find_all('li')
            departments = ', '.join([dept.get_text(strip=True).replace(',', '').strip() for dept in departments_list])
        else:
            departments = "No departments listed"
        url_to_profile="https://my.clevelandclinic.org"+profile_link
        Doctors.append({'Name': name,'Departments':departments,'Hospital':"Cleveland Clinic",'Profile':url_to_profile})
    driver.quit()

df = pd.DataFrame(Doctors)
df.to_csv('ClevelandClinic.csv', index=False) 

#soup.prettify().encode('ascii', errors='ignore').decode()

