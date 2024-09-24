# Hospital AI

## Overview
Hospital AI is a web application designed to scrape and process doctors' profiles from top hospitals, providing a user-friendly interface for users to search and view medical professionals and their specialties.

## Features
- Scrape doctors' profiles, treatments, and departments from the top 50 hospitals' websites.
- Clean and process the scraped data.
- Train a Private GPT model using the cleaned data.

### Setup

1. Clone the Repository
```
git clone https://github.com/Abhishek-Jilowa/Hospital_AI
cd private-gpt
```
2. Install Dependencies
```
pip install -r requirements.txt
```

3. Create and Activate a Virtual Environment
```
pyenv install 3.11
pyenv local 3.11
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
poetry self update 1.8.3
choco install make
PGPT_PROFILES=local
make run
```
4. Go to http://localhost:8001/ for accessing private-gpt.

## Screenshots of Interaction
![Screenshot 2024-09-23 164344](https://github.com/user-attachments/assets/bcda1fa9-ef01-4927-aef9-ab9baaf11e0d)
![Screenshot 2024-09-23 165054](https://github.com/user-attachments/assets/ae649e31-8a15-4b15-aed1-26c53c02bb26)
![Screenshot 2024-09-23 170111](https://github.com/user-attachments/assets/40e945e8-0ce9-4d2f-ba34-04087c27b31a)
![Screenshot 2024-09-24 163808](https://github.com/user-attachments/assets/1e143f9d-2e2c-454a-88bb-2a093decd394)

### Contact
For any questions or feedback, please contact jilowa.1@iitj.ac.in.
