from whoosh import index
from whoosh.fields import Schema, TEXT, ID

from src.preprocess import preprocess

import os
import json
import argparse

parser = argparse.ArgumentParser(description='Create Whoosh index')
parser.add_argument('-d', '--data', type=str, required=True,
                    help='Path to JSON file containing the articles')
parser.add_argument('-i', '--index', type=str, default='indexdir',
                    help='Directory in which to store the index')
args = parser.parse_args()

DATA_PATH = args.data
INDEX_DIR = args.index

os.makedirs(INDEX_DIR, exist_ok=True)

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = index.create_in("indexdir", schema)

writer = ix.writer()
for article in json.load(open(DATA_PATH)):
    writer.add_document(title=article['title'],
                        path=article['link'],
                        content=preprocess(article['summary']))
writer.commit()
