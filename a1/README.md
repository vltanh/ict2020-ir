# Whoosh for News Search

## Info

|Name|Student ID|Mail|
|---|---|---|
|Vũ Lê Thế Anh|20C13002|anh.vu2020@ict.jvn.edu.vn|

## **Setup**

```
conda create -n ir-a1
conda activate ir-a1
conda install python=3.9
conda install whoosh
conda install feedparser
pip install underthesea
```

## **Usage**

### **Build**

```
usage: build_model.py [-h] -d DATA [-o OUTPUT]

Build the Vector Space Model with Term-Document matrix

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  Path to the file containing the documents
  -o OUTPUT, --output OUTPUT
                        Directory to store the model
```

Example:

```
python build_model.py -d data/corpus.txt -o output
```

### **Query**

```
usage: query.py [-h] -q QUERY -d DATA -m MODEL [-k K]

Query from the Vector Space Model with Term-Document matrix

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Query string
  -d DATA, --data DATA  Path to the file containing the documents
  -m MODEL, --model MODEL
                        Path to the file containing the documents
  -k K                  Number of returned document
```

Example:

```
python query.py -q "i love you" -d data/corpus.txt -m output/model.pkl -k 5
```

## **Result**

```
python query.py -q "i love you" -d data/corpus.txt -m output/model.pkl -k 5
```

```
We are no strangers to love
I just wanna tell you how I am feeling
You know the rules and so do I
And if you ask me how I am feeling
A full commitment is what I am thinking of
```
