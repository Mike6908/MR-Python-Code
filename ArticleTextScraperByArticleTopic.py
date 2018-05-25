from bs4 import BeautifulSoup
import urllib
import re
import urllib
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import codecs

biz="^https://www.washingtonpost.com/news/"
pol="^https://www.washingtonpost.com/politics/"
spor="^https://www.washingtonpost.com/news/"
tech="^https://www.washingtonpost.com/news/the-switch/"

linklist = []
html_page = urllib.request.urlopen("https://www.washingtonpost.com/sports")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a', attrs={'href': re.compile(spor)}):
    print(link.get('href'))
    linklist.append(link.get('href'))

nodups = list(set(linklist))

URL = "https://www.washingtonpost.com/news/the-switch/wp/2018/05/04/why-apple-lg-and-others-have-given-in-to-the-notch/"
def get_article_content(url):
    # input: url for a news article
    # output: approx. content of the article
    # Downloads HTML for an article and then
    # pulls data from paragraphs in the html
    paragraph_re = re.compile(r"<p.*/p>")
    tag_re = re.compile(r"<[^>]*>")
    raw_html = urllib.request.urlopen(url).read().decode('utf-8')
    paragraphs = re.findall(paragraph_re, raw_html)
    all_text = " ".join(paragraphs)
    content = re.sub(tag_re, "", all_text)
    return content


contents = get_article_content(URL)
print(contents)

for i,val in enumerate(nodups):
    contents = get_article_content(val)
    #text_file = codecs.open("politics_"+ str(i+51) +".txt", "w", "utf-8")
    text_file = codecs.open("sports_" + str(i+51)+ ".txt", "w", "utf-8")
    #text_file = codecs.open("business_" + str(i+51)+ ".txt", "w", "utf-8")
    #text_file = codecs.open("tech_" + str(i+51)+ ".txt", "w", "utf-8")
    text_file.write(contents)
    text_file.close()

#text_file = codecs.open("business_50.txt", "w", "utf-8")
#text_file = codecs.open("sports_50.txt", "w", "utf-8")
#text_file = codecs.open("politics_test_10.txt", "w", "utf-8")
text_file = codecs.open("tech_53.txt", "w", "utf-8")
text_file.write(contents)
text_file.close()