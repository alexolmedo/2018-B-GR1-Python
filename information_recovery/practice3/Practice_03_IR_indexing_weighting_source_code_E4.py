# -*- coding: UTF-8 -*-
import pickle
import math

index_ltn_file = open('Text_Only_Ascii_Coll_NoSem_index_ltn.txt', 'w')

# Compute ltn weighted index
with open('index.pkl', 'rb') as f:
    index = pickle.load(f)  # Loading index previously stored in disc
    for key, doc_list in index.items():
        for item in doc_list:
            # Apply tf.idf weighting function, consider only 2 decimals
            item[0] = round((1 + math.log10(item[0])) * math.log10(9804 / len(doc_list)), 2)
        # Save to .txt the ltn weigted index
        index_ltn_file.write(str(len(doc_list)) + "=df(" + key + ')\n\t' + str(doc_list) + '\n')

# Save index dictionary in disc
with open('index_ltn.pkl', 'wb') as f:
    pickle.dump(index, f, pickle.HIGHEST_PROTOCOL)
