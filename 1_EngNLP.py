import io
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

dir = sys.argv[1]

# word_tokenize accepts
# a string as an input, not a file.c
stop_words = set(stopwords.words('english'))
file1 = open(dir)
 
# Use this to read file content as a stream:
line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('ketquanlp_eng.txt','a')
        appendFile.write(" "+r)
        appendFile.close()