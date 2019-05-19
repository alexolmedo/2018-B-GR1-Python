# -*- coding: UTF-8 -*-
import pickle
import math

index_bm25_file = open('Text_Only_Ascii_Coll_NoSem_index_bm25.txt', 'w')

# Calculate the length of each document
document_length = {}
with open('index.pkl', 'rb') as f:  # Loading index previously stored in disc
    index_bm25 = pickle.load(f)
    for key, doc_list in index_bm25.items():
        for item in doc_list:
            if item[1] in document_length:
                document_length[item[1]] += item[0]
            else:
                document_length[item[1]] = 1

    k1 = 1.2
    b = 0.75
    avdl = 713
    n = 9804
    for key, doc_list in index_bm25.items():
        for item in doc_list:
            tf = item[0]
            dft = len(doc_list)
            dl = document_length[item[1]]
            # Apply BM25 weighting function, consider only 3 decimals
            item[0] = round(((tf * (k1 + 1)) / (k1 * ((1 - b) + b * (dl / avdl)) + tf)) * math.log10((n - dft + 0.5) / (dft + 0.5)), 3)
        # Save to .txt the bm25 weigted index
        index_bm25_file.write(str(len(doc_list)) + "=df(" + key + ')\n\t' + str(doc_list) + '\n')

# Save index dictionary in disc
with open('index_bm25.pkl', 'wb') as f:
    pickle.dump(index_bm25, f, pickle.HIGHEST_PROTOCOL)
