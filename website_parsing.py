import csv

import requests
from bs4 import BeautifulSoup

res = requests.get("http://portal.tpu.ru/science/konf")
soup = BeautifulSoup(res.content, 'lxml')

data = []
for table_row in soup.select("table.little tr")[5:]:
    col = table_row.find_all("td")
    try:
        if col[1].text != 'Инфомационное сообщение':
            data.append(col[0].text)
            data.append(col[1].text)
    except:
        pass

print(data)

"""
with open("tpu_website_data.csv",'wb') as resultFile:
    wr = csv.writer(resultFile)
    wr.writerows(data)
"""

resultFyle = open("tpu_website_data.csv",'wb')

# Write data to file
for r in data:
    resultFyle.write(r.encode())
resultFyle.close()