# -*- coding: UTF-8 -*-
import pickle
import math

index_ltn_file = open('Text_Only_Ascii_Coll_NoSem_index_bm25.txt', 'w')

# Calculate the length of each document
document_length = {}
with open('index.pkl', 'rb') as f: # Loading index previously stored in disc
    index_ltc = pickle.load(f)
    for key, doc_list in index_ltc.items():
        for item in doc_list:
            if item[1] in document_length:
                document_length[item[1]] += item[0]
            else:
                document_length[item[1]] = 1

print(document_length)


