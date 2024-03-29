# usg_tutorials
```diff
+ Python training tutorials
```
[1. Introduction](#Introduction) <br>
[2. Getting Started](#Getting-Started) <br>
[3. Course Contents](#Course-Contents) <br>

## Introduction
This repository contains tutorials I developed for a series of courses to introduce non-technical individuals to Python.  The training series increases in complexity moving from introduction to more intermediate and finally to some advanced examples of what can be done with Python.  Each level of traning is found on a different branch that can be cloned or downloaded.<br>
<img src="images/training_branches.png">

## Getting Started
*The instructions below assume you already have anaconda installed.  If not, follow the instructions here* <a href="https://docs.anaconda.com/anaconda/install/">anaconda installation instructions</a>
1. Select the branch for the course of interest and Clone or Download the repo using the green button at the top right-hand side of the screen <br>
<img src="images/green_button.png"><br>
2. Each repository comes with a <span>&#42;</span>.yml and requirements.txt.  An environment to run the tutorial in can be created in one of the following ways:

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Option 1`
<blockquote> 
    <p> 
        conda env create -f /path/to/environment.yml 
        <br>conda activate environment
        <br>Be sure to replace environment with the actual name of the .yml file
    </p> 
</blockquote>

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Option 2`
<blockquote> 
    <p> 
        conda create -n yourenvname python=3.7
        <br>conda activate yourenvname
        <br>conda install -c conda-forge --file requirements.txt
    </p> 
</blockquote>

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Option 3`
<blockquote> 
    <p> 
        conda create -n yourenvname python=3.7
        <br>conda activate yourenvname
        <br>conda install pip
        <br>pip install -r requirements.txt
    </p> 
</blockquote>

## Course Contents
1. Introduction
<blockquote> 
    <p> 
        Working with packages and data types 
        <br>Using pandas
        <br>Data cleaning with pandas
        <br>Data visualization
    </p> 
</blockquote>

2. Intermediate
<blockquote> 
    <p> 
        Using APIs and Maps
        <br>Using Nominatim OpenStreetMap's API
        <br>Mapping data & viewing results
        <br>Cleaning and combining data from logs and databases
    </p> 
</blockquote>

3. Advanced
<blockquote> 
    <p> 
        Natural language processing AKA text analytics
        <br>Searching for and visualizing topics in a corpus of documents using gensim and LDAvis
        <br>Name entity recongnition using NLTK
        <br>Looking at word frequency and identifying keywords
    </p> 
</blockquote>


