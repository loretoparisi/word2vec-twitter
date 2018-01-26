#  Word2Vec_Twitter

## About
This repository uses code and model by
[Twitter Word2vec model](https://www.fredericgodin.com/software/) by [Frederic Godin](https://twitter.com/frederic_godin).

This zip contains a word2vec model trained on Twitter data as described in:

Godin, F., Vandersmissen, B., De Neve, W., & Van de Walle, R. (2015).
Multimedia Lab @ ACL W-NUT NER shared task: Named entity recognition for Twitter microposts using distributed word representations.
Workshop on Noisy User-generated Text, ACL 2015.

[Paper](https://fredericgodin.com/papers/Named%20Entity%20Recognition%20for%20Twitter%20Microposts%20using%20Distributed%20Word%20Representations.pdf)

## Disclaimer
Please cite the paper if you use the model.

This zip contains 2 additional files to read the word2vec model with Python.
The code for this was extracted from the Gensim Library which can be found here: https://radimrehurek.com/gensim/models/word2vec.html
The only difference is that it does not use a strict encoding to read the model from the file.
(One can easily integrate, inherit or extend the library or the Python files)

## How to install
```
pip install virtualenv
virtualenv .env
. .env/bin/activate
pip install -r requirements.txt 
```

## Download the Word2vec model
You can download the Word2Vec 400M Twitter model from [here](https://drive.google.com/file/d/10B7cvx3xN7Ef_FxwIO8sigd1J1Ibe6Lu/view?usp=sharing)

## How to run
```
python word2vecReader.py
Loading the model, this can take some time...
The vocabulary size is: 3039345
```

## Running with REPL (Interactive Shell)
```
python
>>> execfile('repl.py')
Loading the model, this can take some time...
The vocabulary size is: 3039345
>>> model
<word2vecReader.Word2Vec instance at 0x1053a4830>
```

## How to use
Load the model into a python script or using REPL, then you can get the most similar words for a term like
```
>>> similar=model.most_similar('cat')
>>> words=list((w[0] for w in similar))
>>> words
[u'dog', u'Cat', u'kitten', u'cats', u'chihuahua', u'kitty', u'pug', u'ferret', u'puppy', u'dogs']
```

or obtain meaningful results like `king – man + women = queen` by adding or subtracting vectors.

```
>>> similar=model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
>>> words=list((w[0] for w in similar))
>>> words
[u'queen']
```

If you want to retrieve the distance as well you can add the 2nd dimension in the array

```
>>> similar=model.most_similar('healthcare')
>>> words=list(((w[0],w[1]) for w in similar))
>>> words
[(u'health-care', 0.7003277540206909), (u'#healthcare', 0.6571943759918213), (u'heathcare', 0.6552523374557495), (u'welfare', 0.621768593788147), (u'medicaid', 0.6213265657424927), (u'higher-ed', 0.6198979616165161), (u'health', 0.6175448894500732), (u'#healthinsurance', 0.6174722909927368), (u'#HIX', 0.6140642166137695), (u'ACA', 0.6094388961791992)]
```

so that you can evaluate the rule `Term 'X' is to term 'Y' as Term 'W' is to term 'Z` like

```
>>> similar=model.most_similar(positive=['boy', 'sister'], negative=['brother'], topn=1)
>>> words=list(((w[0],w[1]) for w in similar))
>>> words
[(u'girl', 0.6565942764282227)]
```

For more information please see [Word2Vec](https://github.com/loretoparisi/word2vec)
```
