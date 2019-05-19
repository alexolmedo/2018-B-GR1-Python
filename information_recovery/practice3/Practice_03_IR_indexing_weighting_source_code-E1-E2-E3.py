# -*- coding: UTF-8 -*-
from html.parser import HTMLParser
from collections import OrderedDict
import zipfile
import time
import pickle
import re
from nltk.stem import PorterStemmer

ps = PorterStemmer()


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
        data = data.replace("/", " ")
        if (self.currentTag == 'docno'):
            self.currentDoc = data
        else:
            if (len(data) > 1):
                # Only letters
                data = re.sub(r'[^a-z\s]', '', data)
                wordlist = str(data).split(" ")
                global docLength
                global numberDocs
                global stopWords
                print(numberDocs)
                numberDocs += 1
                for word in wordlist:
                    # Discard empty strings
                    if word:
                        # Remove stopwords
                        if word not in stopWords:
                            # Apply orter Stemmer
                            word = ps.stem(word)
                            docLength += 1
                            # Check if word already exists in index
                            if word in index:
                                listTemp = list(index[word])
                                # Check if document already exists for certain word
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
                            # If it doesn't exist create new word in index
                            else:
                                index[word] = [[1, self.currentDoc]]


index = {}
parser = MyHTMLParser()
docLength = 0
numberDocs = 0
# Stopword list
stopWords = ["a", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
             "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be",
             "became",
             "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below",
             "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot",
             "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due",
             "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc",
             "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify",
             "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from",
             "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her",
             "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how",
             "however", "hundred", "i", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its",
             "itself",
             "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile",
             "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself",
             "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
             "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or",
             "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per",
             "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious",
             "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some",
             "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take",
             "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter",
             "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those",
             "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward",
             "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was",
             "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas",
             "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever",
             "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your",
             "yours", "yourself", "yourselves", "the", '']

start = time.time()

myzip = zipfile.ZipFile('Text_Only_Ascii_Coll_NoSem.zip', 'r')
myfile = myzip.open('Text_Only_Ascii_Coll_NoSem')
data = myfile.read().decode('utf-8').replace("\n", " ")
# Remove random characters
data = data.replace('’', ' ')
data = data.replace('-', ' ')
data = data.replace('.', ' ')
data = data.replace('=', ' ')
data = data.replace(':', ' ')
data = data.replace(',', ' ')
data = data.replace('\'', ' ')
data = data.replace('\\', ' ')
data = data.replace('_', ' ')
data = data.replace(';', ' ')
data = data.replace('(', ' ')
data = data.replace(')', ' ')
# Remove duplicated spaces
data = " ".join(data.split())
data = data.lower()

parser.feed(data)
print("docLength: " + str(docLength))
print("avfLentgh: " + str(docLength / numberDocs))
print("indexLength: " + str(len(index)))
sortedIndex = OrderedDict(sorted(index.items(), key=lambda x: x[0]))

# Save index .txt file
with open('Text_Only_Ascii_Coll_NoSem_index.txt', 'w') as file:
    for key, value in sortedIndex.items():
        file.write(str(len(value)) + "=df(" + key + ')\n\t' + str(value) + '\n')

# Save index dictionary in disc
with open('index.pkl', 'wb') as f:
    pickle.dump(sortedIndex, f, pickle.HIGHEST_PROTOCOL)

end = time.time()
print("Time : " + str(end - start) + " s")