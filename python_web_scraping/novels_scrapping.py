from bs4 import BeautifulSoup as bs
import requests as req
import re

url = "https://www.gutenberg.org/browse/languages/zh" 
res = req.get(url)
soup = bs(res.text,'lxml')

list_booksurl = []
bookName = []
regex = r"/\d+"


#包含所有中文範圍
for a in soup.select('li.pgdbetext a'):
    if '\u4e00' <= a.text[0] <= '\u9fa5':
        fileName = re.search(regex, a['href'])
        list_booksurl.append('https://www.gutenberg.org/files'+(fileName.group())*2+'-0.txt')
        bookName.append(a.text)
    
# list_booksurl
# bookName

booksurl_text = []
regex01 = r'[^a-zA-Z\s\d*#,.\-:\]\[<>\/\!\"\(\)\@\$\'\%]+'
count = 0
for link in list_booksurl[0:250]:
    res = req.get(link)
    res.encoding = 'UTF-8'
    soup = bs(res.text,'lxml')
    text = re.findall(regex01, soup.text)
    textj = '\n'.join(text)
    path = f'novel/{bookName[count]}.txt'
    f = open(path, 'w', encoding = 'UTF-8')
    f.write(f'書名：{bookName[count]}'+'\n'+textj)
    f.close()
    count += 1