from email import header
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

scraped_data = []


page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
def scrape():
    soup = BeautifulSoup(page.content, "html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')

    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')

        temp_list = []
        
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
            scraped_data.append(temp_list)

    stars_data = []

    for i in range(0,len(scraped_data)):
        Star_names = scraped_data[i][0]
        Distance = scraped_data[i][5]
        Mass = scraped_data[i][8]
        Radius = scraped_data[i][9]
        Lum = scraped_data[i][4]

        require_data = [Star_names,Distance,Mass,Radius,Lum]
        stars_data.append(require_data)
        print(require_data,"eee")
    headers = ['Star_name','Distance','Mass','Radius','Luminosity']

    star_df_1 = pd.DataFrame(stars_data, columns=headers)
    print(scraped_data)
    star_df_1.to_csv("scraped_data.csv",index=True, index_label="id")


        

scrape()







