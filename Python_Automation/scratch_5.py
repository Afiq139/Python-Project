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