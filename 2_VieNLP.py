import io
import sys
import os
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
import codecs
import array as arr




from nltk.corpus import stopwords
from underthesea import word_tokenize #Use 'underthesea lib' instead of 'nltk' for better result
 

dir = sys.argv[1]
with io.open(dir,'r',encoding='utf8') as file:
    text = file.read().replace('\n', '')
text = word_tokenize(text)


stop_words = set(stopwords.words('vietnamese'))
  
filtered_sentence = [w for w in text if not w.lower() in stop_words]
 
filtered_sentence = []
 
for w in text:
    if w not in stop_words:
        filtered_sentence.append(w)
 



for r in filtered_sentence:
    with io.open('ketquanlp_vie.txt','a',encoding='utf8') as file:
        file.write(r + " ")
        file.close()