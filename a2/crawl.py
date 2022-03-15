import feedparser

import json
import os
import argparse

parser = argparse.ArgumentParser(description='Crawl from RSS links')
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Path to the TXT file containing RSS links')
parser.add_argument('-o', '--output', type=str, default='data/articles.json',
                    help='Path to the desired output file')
args = parser.parse_args()

RSS_PATH = args.input
OUTPUT = args.output

data = dict()
for link in open(RSS_PATH).readlines():
    feed = feedparser.parse(link)
    for entry in feed['entries']:
        data[entry['link']] = entry

os.makedirs('data', exist_ok=True)
json.dump(list(data.values()), open(OUTPUT, 'w'))
