# Word Counter Text analyser for Online TXT files.
# CReating at the end a .CSV Excel file

from urllib.request import urlopen
from collections import Counter
from string import punctuation
from time import time
import sys
from pprint import pprint

url = 'https://archive.org/stream/MarxEngelsCollectedWorksVolume10MKarlMarx/Marx%20%26%20Engels%20Collected%20Works%20Volume%201_%20Ka%20-%20Karl%20Marx_djvu.txt'#CHOOSE THE URL

data = urlopen(url).read()

def freq_dist(data):
    """
    :param data: file-like object opened in binary mode or
                 sequence of byte strings separated by '\n'
    :type data: an iterable sequence
    """
    
    punc = punctuation.encode('utf-8')
    words = (word for line in data for word in line.translate(None, punc).decode('utf-8').split())
    return Counter(words)

start = time()
word_dist = freq_dist(data.splitlines())
print('elapsed: {}'.format(time() - start))
pprint(word_dist.most_common(100))

#EXPORT THE OUTPU INTO A CSV FILE: 
import csv

with open('data12.csv', 'w', newline='') as f:#CHOOSE HERE THE NAME OF THE .CSV FILE THAT WILL BE GENERATED!
    writer = csv.writer(f)
    writer.writerows(word_dist.most_common(100))
