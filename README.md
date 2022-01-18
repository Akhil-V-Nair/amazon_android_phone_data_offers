# amazon_android_phone_data_offers
## Web scraped Android Phone Data Analysis

###### 13 days of random phone offers scraped from Amazon based on Brand Filtering, Featured on Page, Page Number, Ratings, Price Range and Today's Deal. These data were scraped during the Great Indian Sale

## Running analysis to find out what phones are likely to be preferred by customers.

###### The Project contains the following files:

1. Combined Android Phone data as a csv file.
2. Webscraper python file.
3. Data Processing jupyter notebook.
4. SQL code used for Database creation( WIP )
5. Screenshot of analysed Power BI Dashboard ( WIP )

# Dashboard Analysis
![Dashboard](https://user-images.githubusercontent.com/73117054/150033164-9b9d79fc-d0a1-456b-b370-6dbfab9189bf.png)

1.We first get to see the costliest phone with lowest ratings and a phone with highest ratings but cheap. This explains that there could be not many who would have purchased these two phones and for the people who purchased the Samsung phone would mean that they were not satisfied with the features or also the phone could have been damaged when received, hence leading to a Low Rating. Even for the highest rated phone we see that the price was low and since this was during an Offer time, they could have just launched this model and the people who might have purchased it, might not have ordered it for themseleves or there couldn't have been many purchases at all.

2.We then see the Average Ratings and Average Prices of the Models.

3.We have number of models for each specifications and for each brand.

4.We have a table of Brand and Models with Specifications color coded based on their ratings, with darker shade being in the range of 4.3 to 5, middle shade being in the range of 3 to 4.3 and the lighter shade being in the range of 0 to 3.

5.We have top 5 models based on their ratings from 4.3 to 5 and price range between 10000-50000.
From this we get to see that One Plus seems to be a popular choice having a decent price for an highly rated phone.
But amazon had failed to sponsor them during the Sale, knowing that One Plus wouldn't need a sponsorship as their Sales in Online is great.

6.There is filter for Brand and Date that interacts with other visuals.

7.Haven't used date much since the data was collected only for a period of 13 days and it is very small data. But the analysis can be applied to a huge dataset by including more features.


# SQL Findings
## 1
![Average Price of each model specs based on quantity and ratings more than 4](https://user-images.githubusercontent.com/73117054/150035321-e7297119-00b1-4692-bf31-d2e816efc673.png)

This gives the Average Price of each Models with Specifications based on Quantity and Ratings being more than 4.

## 2
![Phones in range of 10k and 40k with a rating of atleast 4 3](https://user-images.githubusercontent.com/73117054/150035628-4d3c7a79-ae9c-4183-884e-7ec4c0c09fd9.png)

This gives the Phones that are in range of 10000 and 40000 with at least a rating of 4.3

## 3
![Popular Brand](https://user-images.githubusercontent.com/73117054/150035848-3207650c-42eb-4b55-aac0-4d42f4b1e992.png)

This Query shows us the Popular Brand by calculating the Average Price and Average Ratings among their models


# Outcome

1.From the visualizations and SQL query, we got to see that One Plus is a popular Brand with model being available under 50000 and also having a good Rating for all their models.

2.The data collected is random and small, however if the data is collected on a daily basis without the collection being random, then we should be able to gain more insights and also perform Time Series Analysis on the same.

3.Can identify the dip or increase in ratings or prices depending on time, which would be a great analysis tool for marketting these Phones.

## Note:
This is my second project trying to use the Data Analysis skills and tools that i have been studying about. Any feedback is greatly appreciated.


