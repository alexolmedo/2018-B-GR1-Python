# -*- coding: UTF-8 -*-
import pickle
from nltk.stem import PorterStemmer
from collections import OrderedDict

# Ranked retrieval for the query "web ranking scoring algorithm"
document_rank = {}
with open('index_bm25.pkl', 'rb') as f:
    index_ltn = pickle.load(f)  # Loading index previously stored in disc
    query = "web ranking scoring algorithm"
    ps = PorterStemmer() # Transform the query in a list of stemmed terms
    for w in query.split():
        for item in index_ltn[ps.stem(w)]:
            # Generate dictionary containing the id of a document and its relevance score
            if item[1] in document_rank:
                document_rank[item[1]] += item[0]
            else:
                document_rank[item[1]] = item[0]

# Order de dictionary to get the 10 most relevnt documents
document_rank = OrderedDict(sorted(document_rank.items(), key=lambda x: x[1]))
document_rank = OrderedDict(reversed(list(document_rank.items())))

# Show the results
index = 1
for x in list(document_rank)[0:10]:
    print(str(index) + ". Document: {}, Score: {}".format(x, round(document_rank[x], 4)))
    index += 1
