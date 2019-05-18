# -*- coding: UTF-8 -*-
import pickle
import math

index_ltn_file = open('Text_Only_Ascii_Coll_NoSem_index_ltc.txt', 'w')

# Compute ltc weighted index
with open('index_ltn.pkl', 'rb') as f: # Loading index previously stored in disc
    index_ltc = pickle.load(f)
    for key, doc_list in index_ltc.items():
        # Calculate the lenght of the vector
        square_sum = 0
        for item in doc_list:
            square_sum += item[0]**2
        vector_length = math.sqrt(square_sum)

        # Length normalization
        for item in doc_list:
            try:
                item[0] = round((item[0]/vector_length),3)
            except:
                item[0] = 0.0

        # Save to .txt the normalized index
        index_ltn_file.write(str(len(doc_list)) + "=df(" + key + ')\n\t' + str(doc_list) + '\n')

# Save index dictionary in disc
with open('index_ltc.pkl', 'wb') as f:
    pickle.dump(index_ltc, f, pickle.HIGHEST_PROTOCOL)

