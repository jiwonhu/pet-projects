# Download Singapore's rainfall, temperature, and wind data for 1983~2022
# URL example: http://www.weather.gov.sg/files/dailydata/DAILYDATA_S24_202212.csv

import requests

url_base="http://www.weather.gov.sg/files/dailydata/"
filename_base="DAILYDATA_S24_"

for yr in range(1983, 2023):
  for month in range(1, 13):
    if month < 10:
      date=str(yr)+"0"+str(month)
    else:
      date=str(yr)+str(month)
    filename=filename_base+date+".csv"
    url=url_base+filename
    # download the file
    with open(filename, 'wb') as out_file:
       content=requests.get(url, stream=True).content
       out_file.write(content)