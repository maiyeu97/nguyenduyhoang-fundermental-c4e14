from urllib.request import urlopen
from bs4 import BeautifulSoup # Camel CASE
import pyexcel

raw_data = urlopen('http://www.nhaccuatui.com')
data = raw_data.read()
html_content = data.decode('utf-8')
soup = BeautifulSoup(html_content,'html.parser')
div =soup.find("div","list_show_chart") #find one
li_list = div.find_all("li")

news_list = []
for li in li_list:
    div = li.div # find('h4')
    a = div.a # find ('a')
    news = {
        'singe': list_name_singer.string,
        'link': 'http://nhaccuatui.com' + a['href']
    }
    news_list.append(news)
pyexcel.save_as(records=news_list, dest_file_name="tacgia.xlsx")

# file = open('nct.html','wb')
# file.write(raw_data)
# file.close()
