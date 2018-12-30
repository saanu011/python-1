from bs4 import BeautifulSoup
import urllib.request
 
# specify the url
quote_page = 'http://www.codechef.com'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


#name = name_box.text.strip() # strip() is used to remove starting and trailing
print (soup)