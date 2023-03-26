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

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ....." + file_name)
