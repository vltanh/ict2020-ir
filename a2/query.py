from whoosh import index
from whoosh.qparser import QueryParser

from src.preprocess import preprocess

import argparse

parser = argparse.ArgumentParser(description='Search Whoosh index')
parser.add_argument('-q', '--query', type=str, required=True,
                    help='Query string')
parser.add_argument('-i', '--index', type=str, default='indexdir',
                    help='Directory containing the index')
args = parser.parse_args()

INDEX_DIR = args.index
QUERY = args.query

ix = index.open_dir(INDEX_DIR)

with ix.searcher() as searcher:
    query = preprocess(QUERY)
    query = QueryParser('content', ix.schema).parse(query)
    results = searcher.search(query, limit=None)
    if len(results):
        for result in results:
            print('Title:', result['title'])
            print('Link:', result['path'])
            print('=====')
    else:
        print('Oops! Not found!')
