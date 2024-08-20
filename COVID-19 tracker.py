import pandas as pd
import matplotlib.pyplot as plt
import requests

def fetch_covid_data(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

cases_url = "https://disease.sh/v3/covid-19/countries"
vaccinations_url = "https://disease.sh/v3/covid-19/vaccine/coverage/countries"

cases_df = fetch_covid_data(cases_url)
vaccinations_df = fetch_covid_data(vaccinations_url)

cases_df = cases_df[['country', 'cases', 'deaths', 'recovered', 'population']]
vaccinations_df = vaccinations_df[['country', 'timeline']]

vaccinations_df['vaccinations'] = vaccinations_df['timeline'].apply(lambda x: list(x.values())[-1])

merged_df = pd.merge(cases_df, vaccinations_df[['country', 'vaccinations']], on='country')

merged_df['cases_per_100k'] = (merged_df['cases'] / merged_df['population']) * 100000
merged_df['deaths_per_100k'] = (merged_df['deaths'] / merged_df['population']) * 100000
merged_df['vaccinations_per_100k'] = (merged_df['vaccinations'] / merged_df['population']) * 100000

sorted_df = merged_df.sort_values(by='cases_per_100k', ascending=False).head(10)

plt.figure(figsize=(12, 8))
plt.barh(sorted_df['country'], sorted_df['cases_per_100k'], color='skyblue')
plt.xlabel('Cases per 100,000 People')
plt.title('Top 10 Countries by COVID-19 Cases per 100,000 People')
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(12, 8))
plt.barh(sorted_df['country'], sorted_df['deaths_per_100k'], color='salmon')
plt.xlabel('Deaths per 100,000 People')
plt.title('Top 10 Countries by COVID-19 Deaths per 100,000 People')
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(12, 8))
plt.barh(sorted_df['country'], sorted_df['vaccinations_per_100k'], color='lightgreen')
plt.xlabel('Vaccinations per 100,000 People')
plt.title('Top 10 Countries by COVID-19 Vaccinations per 100,000 People')
plt.gca().invert_yaxis()
plt.show()
