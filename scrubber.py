from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request

# CREATE SOUP
url = "https://www.foxnews.com"
client = request(url) # request session from url
page_html = client.read() # store page into var page_html
client.close() # close connection
page_soup = soup(page_html, "html.parser") # parse as html file
containers = page_soup.findAll("article", {"class":"article"}) # grab every article element with class 'article'

# EXCEL FILE FORMATTING
filename = "articles.csv"
f = open(filename, "w") # open file and begin writing
headers = "TITLE, LINK\n" # list of headers
f.write(headers) # write headers for csv file

# LOOP - GET INFO AND WRITE
for container in containers: # go through all containers
    blobtext = container.find("div", {"class":"info"}) # find info sub-class and store it
    title_text = blobtext.header.h2.a.text # get title name text
    title = title_text.replace(",", "").replace("\n", "").replace("\r", "") # remove comma, newline, and return characters (***)
    link = blobtext.header.h2.a["href"] # get link
    s = title + "," + link + "\n" # concat
    f.write(s) # write row to file
    
    print("TITLE:", title)
    print("LINK:", link)

f.close() # close the spreadsheet when done

# *** Beautiful Soup stores everything like lists, and return characters or newline characters can get stored in as items if you're not careful! Took me about 2 hours to figure this out the hard way...