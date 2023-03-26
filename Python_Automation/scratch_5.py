import requests #getting content of the TED talk page

from bs4 import BeautifulSoup #web scrapping

import re # Regular expression pattern matching

#from urllib.request import urlretrieve # downloading mp4

import sys #for argument parsing

#Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: please enter the TED Talk URL")

#url = "http://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_0f_"
#url = "http://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"

r = request.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

#47.05