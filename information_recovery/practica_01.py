from html.parser import HTMLParser
from operator import itemgetter
from collections import OrderedDict

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
            wordlist = str(data).split(" ")
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
with open("practice_01_documents.xml", 'r', encoding='utf8') as myfile:
    data = myfile.read().replace('\n', '')

data = data.replace('’', ' ')
data = data.replace('  ', ' ')
data = data.lower()

parser.feed(data)

sortedIndex = OrderedDict(sorted(index.items(), key=lambda x: x[0]))

with open('practice_01_results.txt', 'w') as file:
    for key, value in sortedIndex.items():
        file.write(key+' = \n\t'+str(value)+'\n')



