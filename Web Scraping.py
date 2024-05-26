from bs4 import BeautifulSoup
import requests
import pandas as pd
import mysql.connector


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


table = soup.find('table', {'class': 'wikitable sortable'})


world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


df = pd.DataFrame(columns=world_table_titles)


column_data = table.find_all('tr')
for row in column_data[1:]:  
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

print(df)

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',         
        password='',         
        database='companies_db'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS largest_companies (
            rank INT,
            name VARCHAR(255),
            industry VARCHAR(255),
            revenue FLOAT,
            employees INT,
            headquarters VARCHAR(255)
        )
        """)

        for index, row in df.iterrows():
            sql = "INSERT INTO largest_companies (rank, name, industry, revenue, employees, headquarters) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, tuple(row))

        connection.commit()
        print("Data inserted successfully")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
