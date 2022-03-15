import numpy as np
import scipy.sparse as sp
from sklearn.metrics import pairwise

from src.preprocess import preprocess

import pickle
import argparse

parser = argparse.ArgumentParser(
    description='Query from the Vector Space Model with Term-Document matrix')
parser.add_argument('-q', '--query', type=str, required=True,
                    help='Query string')
parser.add_argument('-d', '--data', type=str, required=True,
                    help='Path to the file containing the documents')
parser.add_argument('-m', '--model', type=str, required=True,
                    help='Path to the file containing the documents')
parser.add_argument('-k', type=int, default=10,
                    help='Number of returned document')
args = parser.parse_args()

QUERY = args.query
DATA_PATH = args.data
MODEL_PATH = args.model
K = args.k

# Load model
model = pickle.load(open(MODEL_PATH, 'rb'))
terms_dict = model['terms_dict']
tfidf = model['tfidf']
idf = model['idf']

# Preprocess query
query = preprocess(QUERY)

# Count vector
count = sp.lil_matrix((1, len(terms_dict)))
for term in query:
    idx = terms_dict.get(term, 0)
    count[0, idx] += 1

# Calculate TF for query
tf = count.tocsr()
tf.data = tf.data / \
    np.repeat(
        np.add.reduceat(tf.data, tf.indptr[:-1]),
        np.diff(tf.indptr)
    )

# Calculate TF-IDF for query
query_tfidf = tf @ sp.diags(idf)

# Calculate distance
d = pairwise.cosine_distances(tfidf, query_tfidf)

# Result
data = [x.strip() for x in open(DATA_PATH).readlines()]
result = np.argsort(d.reshape(-1))
for x in result[:K]:
    print(data[x])
