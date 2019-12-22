# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:07:52 2017

@author: JP
"""

import pyutilib.subprocess
import os, errno
from collections import Counter
import chardet
import string
from operator import itemgetter

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import gensim
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim
import numpy as np

import webbrowser



def filefinder(path, file_extension):
    '''
    path = path to location of files you want to grab e.g.-> "C:/Joe/MyDocs/"
    file_extension = file type e.g.-> .txt, .pdf
    '''
    
    lst = []
    
    if not file_extension.startswith("."):
        file_extension = "."+file_extension
    
    with os.scandir(path) as f:
        for entry in f:
            if entry.name.endswith(file_extension) and entry.is_file():
                lst.append(path+"/"+entry.name)
    
    return lst


def pdf2txt(file_list):
    '''
    file_list = a list of file names
    '''
    
    for file in file_list:
        exename = ""
        cmd = exename + " -layout " + file
    
        pyutilib.subprocess.run_command(cmd)
        
    return

def gettext(path,filenames):
    '''
    path = path to location of files you want to load text from e.g.-> "C:/Joe/MyDocs/"
    filenames = list of file names
    '''
    
    encoding = []
    entities = []
    
    for fn in filenames:
        file = path+"/"+fn
        with open(file, "rb") as fh:
            text = fh.read()
            encoding.append(chardet.detect(text)['encoding'])
            
    for i in range(len(filenames)):
        file = path+"/"+filenames[i]
        with open(file, encoding=encoding[i]) as fh:
            text = fh.read() 
            entities.append(ner(text))
            
    return entities

def ner(text, entType=["GPE"]):
    '''
    text = text loaded from a file
    entType = list of Name Entity types (e.g. "PERSON", "ORGANIZATION", "LOCATION", "GPE").Default = "GPE"
    '''
    
    gpes = []
    
    sentences = sent_tokenize(text)
    words = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged = [nltk.pos_tag(w) for w in words]
    entities = [nltk.chunk.ne_chunk(t) for t in tagged]
    e = [entity for entity in [getEntities(node) for node in entities]\
                                 if len(entity)>0]
    for lst in e:
        for etype, entity in lst:
            if etype in entType:
                gpes.append(entity)
    
    return Counter(gpes).most_common(100)
    
def entityStr(e):
  return " ".join([word for (word, pos) in e.leaves()])
 
def getEntities(nodes):
  return [(e.label(), entityStr(e)) \
    for e in nodes if isinstance(e, nltk.tree.Tree)]
  
  
def topics(path, file_extension, n=100, p=20, a='auto', b=1, rand=46):
    '''
    path = path to location of files you want to review e.g.-> "C:/Joe/MyDocs/"
    file_extension = file type e.g.-> .txt, .pdf
    n = number of iterations, default = 100. More iterations takes more time,
    but improves results.
    p = number of training passes through the corpus. 1 is enough for a large corpus.  
    Smaller corpora will benefit from n > 1.
    a = hyperparameter alpha
    b = hyperparameter eta
    rand = random seed value, default = 46.
    '''
        
    encoding = []
    corpus = []
    text_list = []
    files = filefinder(path, file_extension)

    for file in files:
        with open(file, "rb") as fh:
            text = fh.read()
            encoding.append(chardet.detect(text)['encoding'])
            
    for i in range(len(files)):
        with open(files[i], encoding=encoding[i]) as fh:
            text = fh.read()
            corpus.append(text)
            
    stop = set(stopwords.words('english'))
    stop |= set(['like',"it's", 'get', "don't", 'even', "you've", 
                 "you're", "what's", "didn't", "wasn't",
                "doesn't"])
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    
    for doc in corpus:
        stop_free = " ".join([i for i in doc.lower().split() if i.strip() not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        short_free = " ".join(w for w in punc_free.split() if len(w) > 4)
        number_free = " ".join(w for w in short_free.split() if not any(c.isdigit() for c in w))
        normalized = " ".join(lemma.lemmatize(word) for word in number_free.split())
        normalized = normalized.split()
        text_list.append(normalized)
        
    dictionary = corpora.Dictionary(text_list)
    dictionary.save('dictionary.dict')
    
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_list]
    corpora.MmCorpus.serialize('corpus.mm', doc_term_matrix)


    np.random.seed(rand) # setting random seed to get the same results each time.
    Lda = gensim.models.ldamodel.LdaModel
    
    numTopix=3
    nwords=5
  

    ldamodel = Lda(doc_term_matrix, num_topics=numTopix, alpha=a, eta=b,
                   id2word=dictionary, passes=p, iterations=n)
    
    ldamodel.save('topic.model')
    
    loading = LdaModel.load('topic.model') 

    topics = loading.print_topics(num_topics=numTopix, num_words=nwords)
    
    for topic, vocab in topics:
        print("Top {} words in Topic {}:".format(nwords, topic))
        print(vocab, "\n")


    for i in range(len(text_list)):        
        bow = ldamodel.id2word.doc2bow(text_list[i])
#        print(files[i].split("\\")[-1]," ---> ", ldamodel.get_document_topics(bow))
        lis = ldamodel.get_document_topics(bow)
        top = max(lis,key=itemgetter(1))[1]
        topic = [ (t,s) for t, s in lis if s  == top ]
        print(files[i].split("\\")[-1]," ---> Topic {}".format(topic[0][0]), "\n" )    

    print("For more information see: https://radimrehurek.com/gensim/models/ldamodel.html")
    return


def word_find(line,words):
    return list(set(line.strip().split()) & set(words))

def searchtext(path,filenames,low):
    '''
    path = path to location of files you want to search e.g.-> "C:/Joe/MyDocs/"
    filenames = list of file names
    low = list of words to be searched for
    '''

    encoding = []
    matches = []
    
    for fn in filenames:
        file = path+"/"+fn
        with open(file, "rb") as fh:
            text = fh.read()
            encoding.append(chardet.detect(text)['encoding'])
            
    for i in range(len(filenames)):
        file = path+"/"+filenames[i]
        with open(file) as fh:
            for idx,line in enumerate(fh, start=1):
                common = word_find(line,low)
                if common:
                    match = (filenames[i], "".join(common))
                    matches.append(match)
            
    return matches



def silentremove(filename):
    '''
    filename = name of a file to remove from directory
    '''
    try:
        os.remove(filename)
    except OSError as e: 
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred
            
    return
            
            
def viewhtml(html):
    '''
    html = .html file to open
    '''
    
    with open(html, 'r') as input_file, open('temp.html', 'w') as output_file:
        for line in input_file:
            if line.strip() == 'to replace':
                output_file.write('new line\n')
            else:
                output_file.write(line)
            
    silentremove(html)
    os.rename('temp.html', html)
    
    webbrowser.open(html)
    
    
    return
   

