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


### Contact
For any questions or feedback, please contact jilowa.1@iitj.ac.in.
