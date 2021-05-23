import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from collections import Counter


def ignore_punctuation(common_word):
    common_word = common_word.replace('.', '')
    common_word = common_word.replace(':', '')
    common_word = common_word.replace(',', '')
    common_word = common_word.replace('"', '')
    common_word = common_word.replace('\'', '')
    common_word = common_word.replace('-', '')
    common_word = common_word.replace('!', '')
    common_word = common_word.replace('?', '')
    common_word = common_word.replace('+', '')
    common_word = common_word.replace('/', '')
    common_word = common_word.replace('*', '')
    return common_word.lower()
#url = "https://www.walla.co.il"
url = input("Enter URL:")
for i in url:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")




# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

revised_words_in_page_list = list()
for word in text.split(' '):
    if not bool(re.search(r'\d', word)):
        revised_words_in_page_list.append(ignore_punctuation(word))

def create_dictionary(clean_list):
    print("started dict")
    word_count = {}
    for word in revised_words_in_page_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    c = Counter(word_count)
    # returns the most occurring elements
    top = c.most_common(10)
    print(top)
create_dictionary(revised_words_in_page_list)
    
