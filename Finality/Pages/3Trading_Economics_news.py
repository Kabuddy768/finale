import streamlit as st
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
from textblob import TextBlob

def scrape_news():
    url = 'https://tradingeconomics.com/kenya/news'
    chromedriver_path = r'C:\Users\Ben\Desktop\chrome\chrome-win64\chromedriver.exe'

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    driver.quit()

    stream_div = soup.find('div', id='stream')

    news_data = []
    if stream_div:
        for li in stream_div.find_all('li', class_='list-group-item te-stream-item'):
            item_id = li['id']
            title = li.find('a', class_='te-stream-title').b.text
            link = li.find('a', class_='te-stream-title')['href']
            country = li.find('a', class_='te-stream-country').text
            category = li.find('a', class_='te-stream-category').text
            next_sibling = li.div.div.next_sibling
            description = next_sibling.strip() if next_sibling else ""
            date = li.small.text

            # Extract text
            text = li.div.div.find_next('div').find_next('div').find_next('div').get_text(strip=True)

            # Remove any HTML tags from the text string
            clean_text = re.sub(r'<.*?>', '', text)

            # Analyze sentiment using TextBlob
            blob = TextBlob(clean_text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            news_data.append({
                "Item ID": item_id,
                "Title": title,
                "Link": link,
                "Country": country,
                "Category": category,
                "Description": description,
                "Content": text,
                "Clean Content": clean_text,
                "Date": date,
                "Polarity": polarity,
                "Subjectivity": subjectivity,
            })

    return news_data

def main():
    st.title("Trading Economics News Scraper")

    # Scrape news data
    news_data = scrape_news()

    # Display news data in Streamlit
    st.subheader("News Data")
    for news_item in news_data:
        st.write(f"**Item ID:** {news_item['Item ID']}")
        st.write(f"**Title:** {news_item['Title']}")
        st.write(f"**Link:** {news_item['Link']}")
        st.write(f"**Country:** {news_item['Country']}")
        st.write(f"**Category:** {news_item['Category']}")
        st.write(f"**Description:** {news_item['Description']}")
        st.write(f"**Date:** {news_item['Date']}")
        st.write(f"**Polarity:** {round(news_item['Polarity'], 2)}")
        st.write(f"**Subjectivity:** {round(news_item['Subjectivity'], 2)}")
        #st.write(f"**Text:** {news_item['Clean Content']}\n")
        st.markdown("---")

if __name__ == "__main__":
    main()