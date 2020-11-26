import sys
import requests
from datetime import datetime
import pandas as pd


def downloadReport(start_date,end_date):
    #Specify start and end date
    #start_date = '2020-05-01'
    #end_date = '2020-05-24'
    date_to_scrape = pd.date_range(start=start_date,end=end_date).to_list()
    total_dates = len(date_to_scrape)
    i = 0
    while i < total_dates:
        date = str(date_to_scrape[i])[0:10]
        d = datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%y')
        #get url
        url = f'https://nsong.org/DownloadHandler.ashx?FileName=DailyOperationalRpt{d}.pdf'
        r = requests.get(url, allow_redirects=True)
        #download the content
        open(f'DailyOperationalRpt{d}.pdf', 'wb').write(r.content)
        print(f"Downloaded DailyOperationalRpt{d}.pdf")
        i +=1


#if __name__ == "__main__":
   # downloadReport('2020-02-01', '2020-04-30')