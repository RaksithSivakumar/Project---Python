import requests
import pandas as pd
from bs4 import BeautifulSoup
from pyairtable import Api

# Airtable Configuration
api_key = "patPsJygEimD5q4VI.5d2f3d3e9320c84b484764def8c3ea249f412947f1aca50e913398adb2c8ac54"
base_id = "appQf1DnnbBl8WZXp"
table_name = "Companies"

api = Api(api_key)
airtable_table = api.table(base_id, table_name)

# Step 1: Scrape Wikipedia table
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Find the desired table
table = soup.find('table', {'class': 'wikitable sortable'})
headers = [header.text.strip() for header in table.find_all('th')]

# Create a DataFrame
df = pd.DataFrame(columns=headers)

# Extract and append rows
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    values = [cell.text.strip() for cell in cells]
    if len(values) == len(df.columns):
        df.loc[len(df)] = values

# Step 2: Data Cleaning
df['Rank'] = df['Rank'].str.replace('[^\d]', '', regex=True).astype(int)
df['Revenue (USD millions)'] = df['Revenue (USD millions)'].str.replace('[^\d.]', '', regex=True).astype(float)
df['Employees'] = df['Employees'].str.replace('[^\d]', '', regex=True).astype(int)

print("Cleaned DataFrame:\n", df.head())

# Step 3: Upload to Airtable
# FIRST check your Airtable field names and adjust these to match exactly:
FIELD_NAMES = {
    'rank': 'Rank',  # Airtable field name: Your field name
    'name': 'Name',
    'industry': 'Industry',
    'revenue': 'Revenue (USD millions)',  # This needs to match your Airtable's revenue field name
    'employees': 'Employees',
    'hq': 'Headquarters'
}

for index, row in df.iterrows():
    record = {
        FIELD_NAMES['rank']: row['Rank'],
        FIELD_NAMES['name']: row['Name'],
        FIELD_NAMES['industry']: row['Industry'],
        FIELD_NAMES['revenue']: row['Revenue (USD millions)'],
        FIELD_NAMES['employees']: row['Employees'],
        FIELD_NAMES['hq']: row['Headquarters']
    }
    
    try:
        airtable_table.create(record)
        print(f"✅ Successfully inserted record {index + 1}: {row['Name']}")
    except Exception as e:
        print(f"❌ Error inserting record {index + 1} ({row['Name']}): {str(e)}")

print("✅ Data insertion process completed.")