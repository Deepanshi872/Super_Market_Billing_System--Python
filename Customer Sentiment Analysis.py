from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
import string
from statistics import mean

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

url = """https://www.flipkart.com/apple-iphone-15-green-128-gb/product-reviews/itm235cd318bde73?pid=MOBGTAGPYYWZRUJX&lid=LSTMOBGTAGPYYWZRUJXUGY7PM&marketplace=FLIPKART"""
driver = webdriver.Chrome()
driver.get(url)

names = []
cities = []
review_date = []
review = []

for page in range(2, 5):
    soup = BeautifulSoup(driver.page_source, "html.parser")

    Names = soup.find_all("p", {"class": "_2NsDsF AwS1CA"})
    for name in Names:
        names.append(name.text)
    print(names)

    Cities = soup.find_all("p", {"class": "MztJPv"})
    for city in Cities:
        cities.append(city.text)
    print(cities)

    Review_date = soup.find_all("p", {"class": "_2NsDsF"})
    for date in Review_date:
        review_date.append(date.text)

    filtered_date = review_date[1::2]
    print(filtered_date)

    Review = soup.find_all("div", {"class": "ZmyHeo"})
    for rev in Review:
        review.append(rev.text)
    print(review)

    time.sleep(5)
    try:
        driver.find_element(By.XPATH, """/html/body/div[3]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]""").click() 
        time.sleep(5)
    except:
        print("next link is not clickable")
        break

    url = """https://www.flipkart.com/apple-iphone-15-green-128-gb/product-reviews/itm235cd318bde73?pid=MOBGTAGPYYWZRUJX&lid=LSTMOBGTAGPYYWZRUJXUGY7PM&marketplace=FLIPKART"""
driver = webdriver.Chrome()
driver.get(url)

names = []
cities = []
review_date = []
review = []

for page in range(2, 5):
    soup = BeautifulSoup(driver.page_source, "html.parser")

    Names = soup.find_all("p", {"class": "_2NsDsF AwS1CA"})
    for name in Names:
        names.append(name.text)
    print(names)

    Cities = soup.find_all("p", {"class": "MztJPv"})
    for city in Cities:
        cities.append(city.text)
    print(cities)

    Review_date = soup.find_all("p", {"class": "_2NsDsF"})
    for date in Review_date:
        review_date.append(date.text)

    filtered_date = review_date[1::2]
    print(filtered_date)

    Review = soup.find_all("div", {"class": "ZmyHeo"})
    for rev in Review:
        review.append(rev.text)
    print(review)

    time.sleep(5)
    try:
        driver.find_element(By.XPATH, """/html/body/div[3]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]""").click() 
        time.sleep(5)
    except:
        print("next link is not clickable")
        break

print(f"Names: {len(names)}, Cities: {len(cities)}, Review_date: {len(filtered_date)}, Review: {len(review)}")

min_length = min(len(names), len(cities), len(filtered_date), len(review))
names = names[:min_length]
cities = cities[:min_length]
filtered_date = filtered_date[:min_length]
review = review[:min_length]

df = pd.DataFrame({
    "Names": names,
    "Cities": cities,
    "Review_date": filtered_date,
    "Review": review
})
df["Review"] = df["Review"].str.lower()
print(df)

df["Reviews_t"] = df["Review"].apply(sent_tokenize)
print(df["Reviews_t"])

def get_polarity(sentences):
    return [TextBlob(sentence).sentiment.polarity for sentence in sentences]

df['Polarity'] = df["Reviews_t"].apply(get_polarity)

def calculate_average_polarity(polarities):
    return mean(polarities) if polarities else 0

df['Average_Polarity'] = df['Polarity'].apply(calculate_average_polarity)
print(df["Average_Polarity"].mean())

