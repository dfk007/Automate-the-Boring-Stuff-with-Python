import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistant_addr') is None)
print(spanElem.attrs)
