#Import Libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import date
import csv

#Connect to website
#Phone offers data in Amazon.
#Featured phones in page one of Amazon
URL = "https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A1805560031%2Cp_n_specials_match%3A21618256031%2Cp_n_condition-type%3A8609960031%2Cp_89%3AOnePlus&dc&qid=1633679651&rnid=3837712031&ref=sr_nr_p_89_2"

#Setting up Selenium
driver = webdriver.Chrome('chromedriver.exe')
driver.get(URL)
time.sleep(10)
website_html = driver.page_source.encode('utf-8').strip()

#Creating Soup Object
soup = BeautifulSoup(website_html,"html.parser")



def data_collection():
    title = soup.find_all(name = "span", class_ = "a-size-base-plus a-color-base a-text-normal")
    all_specs = [specs.getText() for specs in title]
    brands = [items.split(' ', 1)[0] for items in all_specs]  #Brand

    phones = [text.split(')')[0].split('(') for text in all_specs]  
    spec = []
    for i in phones:
        for j in i:
            spec.append(j)
    model = spec[::2]             #Model

    specifications = spec[1::2]   #Specs

    s_price_obj = soup.find_all(name = "span", class_ = "a-price-whole")
    selling_price = [price.getText() for price in s_price_obj]   #Price

    review_obj = soup.find_all(name = "span", class_ = "a-icon-alt")
    review = [ratings.getText() for ratings in review_obj]  
    review = review[:24]          #Ratings

    Date = date.today()
    Date = [str(Date)]*24   #Date

    data = [brands, model, specifications, selling_price, review, Date]

    return data

header = ["Brand", "Model", "Specs", "Price", "Ratings out of 5", "Date"]

with open('AmazonWebScrapper.csv', 'w', newline='',encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data_collection())
    file.close()

#The above file is now created with Today's(22nd of September) data.
#Successding day days, we run the file with updated link and get the data for the day again.
#Data collected for each day is cleaned and transformed using PowerBI to run a complete analysis after the Great Indian Sale.
#Once cleaned the csv will be deleted for it to be created again the next day and the cleaned csv file for each day is saved individually.
#This will go on till the end of Great Indian Sale to observe if there was
#any changes or promotions done to the first page of Amazon.
#The time in which the data is pulled will be random and only when the Great Indian Sale
#begins, we pull the data at 12:00am.

   

