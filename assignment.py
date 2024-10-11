import requests
import selectorlib
import smtplib, ssl
import os
from datetime import datetime
import time


url = 'http://programmer100.pythonanywhere.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Get the current date and time
now = datetime.now()

# Format it as: year-month-day-hour-minute-second (24-hour format)
formatted_datetime = now.strftime('%Y-%m-%d-%H-%M-%S')


def scrape(url):
    """Scrape the url""" 
    response = requests.get(url, headers= HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract2.yaml')
    value = extractor.extract(source)['home']
    return value

def store(extracted):
    with open('date.txt' ,'a') as file:
        file.write(formatted_datetime)
        file.write(f",{extracted}" + '\n')


with open('date.txt', 'r') as file:
    data = file.readlines()
dates = []
temperatures = []

# Loop through the data
for entry in data:
    # Split each string by the comma
    date, temperature = entry.split(',')
    # print(temperature)
        
    # Add to respective lists
    dates.append(date)
    temperatures.append(temperature)
cleaned_temperatures = [temp.strip() for temp in temperatures]

scraped = scrape(url)
extracted = extract(scraped)
print(extracted)
addition = store(extracted)
        
        
                