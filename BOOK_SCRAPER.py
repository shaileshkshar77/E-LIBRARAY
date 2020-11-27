import requests
from bs4 import BeautifulSoup
import csv

mozilla_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
headers = {'User-Agent': mozilla_agent}

main_url = 'https://www.freetechbooks.com/topics'
r = requests.get(main_url, headers=headers)
page = 1
field_names= ['title', 'author','size','download_link']

print('Start scraping {}'.format(main_url))

with open('book.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    writer.writeheader() 

while page < 82:
    bsObj = BeautifulSoup(r.content, 'html.parser')
    links_per_page = bsObj.findAll('p', {'class': 'media-heading lead'})
    for link in links_per_page:
        link_page = requests.get(link.a['href'], headers=headers)
        print('---------------------------------------------------------------')
        try:
            book_title = link.a.get_text()
            print(book_title)
        except:
            book_title = 'not found'
        newbsObj = BeautifulSoup(link_page.content, 'html.parser')
        try:
            download_link = newbsObj.find('div', {'id': 'srvata-content'}).a['href']
            print(download_link)
        except:
            download_link = 'no download link found'
        try:
            author_data = newbsObj.findAll('div', {'class': 'media-body'})[1].findAll('a')
            for data in author_data:
                if data.find('i', 'fa-user'):
                    author = data.get_text().lstrip()
                    print(author)
        except:
            author = 'not found'

        # File size is not available here.
        size = 'not found'

        # Category is not available here.
        category = 'not found'


        book_obj = [
                {'title':book_title, 'author':author,'size':size,'download_link':download_link}
        ]
        print(book_title)
        with open('book.csv', 'a') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = field_names) 
            #writer.writeheader() 
            writer.writerows(book_obj) 
        