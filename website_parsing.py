
import requests
from bs4 import BeautifulSoup

res = requests.get("http://portal.tpu.ru/science/konf")
soup = BeautifulSoup(res.content, 'lxml')


for table_row in soup.select("table.little tr")[5:]:
    col = table_row.find_all("td")
    try:
        if col[1].text != 'Инфомационное сообщение':
            print(col[0].text)
            print(col[1].text)
    except:
        pass



