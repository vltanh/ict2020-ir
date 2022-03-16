# Bag of Word Model Analysis

## Info

|Name|Student ID|Mail|
|---|---|---|
|Vũ Lê Thế Anh|20C13002|anh.vu2020@ict.jvn.edu.vn|

## Solution

### Question

```
Please analyze some pros and cons when applying the Bag of Word Model to a search engine. Show pieces of evidence to illustrate your points.
```

### Answer

**Pros**:

1. It is a simple to implement and is scalable in terms of memory with the sparse matrix data structure and sparse operations (including sparse k-nearest neighbors search).
2. It can handle unknown terms using the [UNK] token which does not affect the performance. Since all tokens from the corpus is accounted for, the subspace of the [UNK] token is null for the database. Hence, every query having the [UNK] will be treated the same.
3. It is recall oriented. It will not miss any words in the query, unless the word is too common (that TDF is low).

**Cons**:

1. It does not take grammar into account nor does it strive to get a hollistic semantic understanding of the document. For example, "school I to go" does not make sense but it is still a match with the grammatically correct "I go to school".
2. It disregards the order of the terms, which is determinantal when it comes to semantic meaning. For example, "A loves B" is different from "B loves A", but is the same under the BoW model.
3. Since it is based on the statistics of the terms and documents, it requires a large corpus to obtain a close approximation of the true statistics.
4. It is not precision-oriented, the retrieved result may only be loosely connected based on statistics but not semantics (see Cons 1 and 2).
