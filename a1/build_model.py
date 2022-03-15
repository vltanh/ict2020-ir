import numpy as np
import scipy.sparse as sp

from src.preprocess import preprocess

import os
import pickle
import argparse

parser = argparse.ArgumentParser(
    description='Build the Vector Space Model with Term-Document matrix')
parser.add_argument('-d', '--data', type=str, required=True,
                    help='Path to the file containing the documents')
parser.add_argument('-o', '--output', type=str, default='output',
                    help='Directory to store the model')
args = parser.parse_args()

CORPUS_PATH = args.data
OUTPUT_DIR = args.output

# Load documents from corpus
docs = list(open(CORPUS_PATH).readlines())
# Preprocess each document
docs = [preprocess(doc) for doc in docs]

# Build vocabulary
unique_terms = set()
for doc in docs:
    unique_terms.update(doc)
unique_terms = sorted(unique_terms)
unique_terms.insert(0, '[UNK]')

# Build mapping from term in vocabulary to identifier (index)
terms_dict = {
    term: i
    for i, term in enumerate(unique_terms)
}

# Compute the sparse count matrix
count = sp.lil_matrix((len(docs), len(terms_dict)))
for i, doc in enumerate(docs):
    for term in doc:
        count[i, terms_dict[term]] += 1

# Compute the TF (for each term and document)
tf = count.tocsr()
tf.data = tf.data / \
    np.repeat(
        np.add.reduceat(tf.data, tf.indptr[:-1]),
        np.diff(tf.indptr)
    )

# Compute the IDF (for each term)
idf = np.log(len(docs) / (tf.getnnz(0) + 1))

# Compute the TF-IDF database
tfidf = tf @ sp.diags(idf)

# Save the model
model = dict()
model['terms_dict'] = terms_dict
model['tfidf'] = tfidf
model['idf'] = idf

os.makedirs(OUTPUT_DIR, exist_ok=True)
pickle.dump(model, open(f'{OUTPUT_DIR}/model.pkl', 'wb'))
