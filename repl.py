#!/usr/bin/env python

import os
import sys
from word2vecReader import Word2Vec

os.environ['PYTHONINSPECT'] = 'True'

model_path = "./word2vec_twitter_model.bin"
print("Loading the model, this can take some time...")
model = Word2Vec.load_word2vec_format(model_path, binary=True)
print("The vocabulary size is: "+str(len(model.vocab)))