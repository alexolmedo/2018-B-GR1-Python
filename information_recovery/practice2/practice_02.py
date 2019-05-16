from html.parser import HTMLParser
from collections import OrderedDict
from os import listdir
import time
import gzip
import re

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []
        self.currentTag = ''
        self.currentDoc = ''

    def handle_starttag(self, tag, attrs):
        self.currentTag = tag
        if self.recording:
            self.recording += 1
            return
        else:
            self.recording = 1
            return

    def handle_endtag(self, tag):
        self.currentTag = ''
        self.recording -= 1

    def handle_data(self, data):
        if (self.currentTag == 'docno'):
            self.currentDoc = data
        else:
            data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
            wordlist = str(data).split(" ")
            global docLength
            global numberDocs
            docLength += len(wordlist)
            numberDocs += 1
            for word in wordlist:
                # check if word already exists in index
                if word in index:
                    listTemp = list(index[word])
                    # check if document already exists for certain word
                    duplicatedDoc = False
                    for doc in listTemp:
                        if (doc[1] == self.currentDoc):
                            duplicatedDoc = True
                            doc[0] += 1
                    if (duplicatedDoc):
                        index[word] = listTemp
                    else:
                        listTemp.append([1, self.currentDoc])
                        index[word] = listTemp
                # if it doesn't exist create new word in index
                else:
                    index[word] = [[1, self.currentDoc]]


index = {}
parser = MyHTMLParser()
docLength = 0
numberDocs = 0

listaArchivos = listdir('Practice_02_data')

for indice, archivo in enumerate(listaArchivos):
    start = time.time()
    with gzip.open("Practice_02_data/" + archivo, 'rt', encoding='utf8') as myfile:
        data = myfile.read().replace('\n', '')

    data = data.replace('’', ' ')
    data = data.replace('  ', ' ')
    data = data.lower()

    parser.feed(data)
    print("docLength: " + str(docLength))
    print("avfLentgh: " + str(docLength / numberDocs))
    print("indexLength: " + str(len(index)))
    sortedIndex = OrderedDict(sorted(index.items(), key=lambda x: x[0]))

    with open(archivo + '_index.txt', 'w') as file:
        for key, value in sortedIndex.items():
            file.write(key + ' = \n\t' + str(value) + '\n')
    end = time.time()
    print("File " + str(indice) + ": " + str(end - start) + " s")
