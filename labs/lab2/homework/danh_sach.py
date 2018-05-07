from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
itune_page = urlopen('https://www.apple.com/itunes/charts/songs/')
data = itune_page.read()
html_content = data.decode('utf-8')
soup = BeautifulSoup(html_content, 'html.parser')
# div = soup.find('div', 'section-content')
news_list = soup.select('.section-content li h4 a')
# print(news_list)

# pyexcel.save_as(records=news_list, dest_file_name="singer_top_song.xlsx")
