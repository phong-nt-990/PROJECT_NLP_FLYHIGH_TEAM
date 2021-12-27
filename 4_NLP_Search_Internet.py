
import io
import sys


from magic_google import MagicGoogle
import pprint
import io
import sys
import os
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
import codecs
import array as arr
types_of_encoding = ["utf8", "cp1252"]
def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()
dir = sys.argv[1]

with io.open(dir,'r',encoding='utf8') as file:
    data = file.read().replace('\n', '')

PROXIES = []

mg = MagicGoogle(PROXIES)


for url in mg.search_url(query=data):
    pprint.pprint(url)
    #####################################################################
