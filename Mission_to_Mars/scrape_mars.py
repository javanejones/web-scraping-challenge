# import necessary libraries
from flask import Flask, render_template
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_data
collection = db.mars_facts

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def index():

def mars():
    #set up driver
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# visualize website
url = "https://mars.nasa.gov/news/"
browser.visit(url)

#create a object
html = browser.html
soup = bs(html,"html.parser")

#Print title and para 
news_title = soup.find("div", class_="content_title").text
news_p = soup.find("div", class_="article_teaser_body").text

#identify the image loca
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(featured_image_url)
from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(featured_image_url))

#Design an path selector to grab the image
xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"

#get image url using bs
html_image = browser.html
soup = bs(html_image, "html.parser")
img_url = soup.find("img", class_="fancybox-image")["src"]
featured_image_url = base_url + img_url

# Mars Facts
facts = "https://space-facts.com/mars/"
tables = pd.read_html(facts)
tables

#clean up table and create html
type(tables)
df = tables[0]
df.columns =  ["Description", "Mars"]
df
df.set_index(["Description"])
df.to_html('table.html')

#connect to chrome driver to gather images
hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemisphere)

#identify and gather images
image_url = []
hemisphere_image_urls = ['Valles Marineris', 'Cerberus', 'Schiaparelli', 'Syrtis Major']
for i in hemisphere_image_urls:
    browser.click_link_by_partial_text(i)
    html = browser.html
    soup = bs(html, 'html.parser')
    title = soup.find('h2', class_= 'title').text
    img = 'https://web.archive.org/' + soup.find('img', class_ = 'wide-image')['src']
    image_url.append({'title' : title, 'img': img})
    
    print(image_url)

return render_template ('index.html')

if __name__ == "__main__":
    app.run(debug=True)

