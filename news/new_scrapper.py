import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find_all('h3')

for headline in headlines:
    print(headline.text.strip())


#######################################

import sqlite3
import time

def delete_data_from_database():
    # Connect to database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Delete all data from table
    c.execute("DELETE FROM mytable")

    # Commit changes and close connection
    conn.commit()
    conn.close()

def save_data_to_database():
    # Connect to database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, data TEXT)''')

    # Insert data into table
    c.execute("INSERT INTO mytable (data) VALUES ('my data')")

    # Commit changes and close connection
    conn.commit()
    conn.close()

while True:
    delete_data_from_database()
    save_data_to_database()
    time.sleep(43200)  # Sleep for 12 hours
    
# This code first deletes all data from the mytable table using the DELETE FROM statement 1. 
# Then it inserts new data into the table using the same method as before. 
