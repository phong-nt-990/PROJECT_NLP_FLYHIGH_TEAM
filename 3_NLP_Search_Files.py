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
dir2 = sys.argv[2]


with io.open(dir,'r',encoding='utf8') as file:
    data = file.read().replace('\n', '')


# get file ketqua.txt
# os.chdir(dir2)
os.system('dir /b /a-d '+ dir2+ " > 5e95d803.tmp")
#dir folder 
fo = open("5e95d803.tmp", "r")
tmps = []
with open ("5e95d803.tmp") as textFile:
    for line in textFile:
        tmp = line.strip()
        tmps.append(tmp)
#get list of file to tmps array
fo.close()
os.remove("5e95d803.tmp")
os.chdir(dir2)
ratiocalc = 0
ratioMAX = 0
i = 0
ratioarray = []
name = []
for x in tmps:
    with io.open(x,'r',encoding='utf8') as file199111:
        dataclone = file199111.read().replace('\n', '')
        tmp1234 = similar (data, dataclone) 
        ratioarray.append(tmp1234)
        name.append(x)



#so sánh
for j in range(len(ratioarray)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(ratioarray)-1:
        #comparing the adjacent elements
        if ratioarray[i]<ratioarray[i+1]:
            #swapping
            name[i],name[i+1] = name[i+1],name[i]
            ratioarray[i],ratioarray[i+1] = ratioarray[i+1],ratioarray[i]
            
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break

unique_l = sorted(set(name), key=name.index)

print ("Files that are most similar to the given content")
for i in range(len(unique_l)):
    print (unique_l[i])
    if i == 4:
        break