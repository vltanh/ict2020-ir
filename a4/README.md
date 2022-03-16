# Bag of Word Model Analysis

## Info

|Name|Student ID|Mail|
|---|---|---|
|Vũ Lê Thế Anh|20C13002|anh.vu2020@ict.jvn.edu.vn|

## Solution

### Question

```
All of the search engines are based on the idea of the term-document matrix concept. 
To transfer from textual search to visual search, what can be understood as "document" and "term" in a visual search system.
Please show pros and cons for each of the points.
```

### Answer

In visual search, the `document` will usually be each of the target of interests. If the problem involves images, each image is one document. If the problem involves videos, each video is a document. If the problem involves 3D objects, each object is a document. We restrict the discussion to only image retrieval system. Other types of target will have similar counterpart of what will be discussed.

There are many things that can be considered a `term`, it however should be defined by a metric space (has a range and a distance function):

1. Patch: for example, 3x3 patches of an image flattened as 9-d vectors

    a. Pros:

        - Simple and fast to compute

    b. Cons:

        - Contains raw unprocessed information
        - Not robust against noises, transformations, or lighting conditions
2. Keypoint descriptors using SIFT or similar algorithms: for example, 128-d vectors from SIFT

    a. Pros:

        - Simple and fast to compute
        - Robust to multiple transformations (scale, rotation, etc.) and lighting conditions 

    b. Cons:

        - The amount of information is limited
        - Not robust against noises

3. Keypoint/Patch descriptors using deep learning:

    a. Pros:

        - Robust to multiple transformations and lighting conditions, as well as noises
        - Contains lots of information

    b. Cons:

        - Requires a large dataset to train a good neural network (as embedder)
        - Requires huge resource
        - Slow to compute
