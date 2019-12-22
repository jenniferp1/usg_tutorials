# usg_tutorials
```html<font color="green">Python training tutorials</font>```

## Introduction
This repository contains tutorials I developed for a series of courses I developed to introduce non-technical individuals to Python.  The training series increases in complexity moving from introduction to more itermediate and finally to some advanced examples of what can be done with Python.  Each level of traning is found on a different branch that can be cloned or downloaded.

## Getting Started
*The instructions below assume you already have anaconda installed.  If not, follow the instructions here* <a href="https://docs.anaconda.com/anaconda/install/">anaconda installation instructions</a>
1. Select the branch for the course of interest and <font color="green">Clone or Download</font> using the green button at the top right-hand side of the screen <br>
2. Each repository comes with a <span>&#42;</span>.yml and requirements.txt.  An environment to run the tutorial in can be created in one of the following ways:<br>
<font color="green">Option 1</font>
<blockquote> 
    <p> 
        `conda env create -f /path/to/environment.yml` 
        <br>`conda activate environment`
        <br>Be sure to replace environment with the actual name of the .yml file
    </p> 
</blockquote>

<font color="green">Option 2</font>
<blockquote> 
    <p> 
        `conda create -n yourenvname python=3.7`
        <br>`conda activate yourenvname`
        <br>`conda install -c conda-forge --file requirements.txt`
    </p> 
</blockquote>

<font color="green">Option 3</font>
<blockquote> 
    <p> 
        `conda create -n yourenvname python=3.7`
        <br>`conda activate yourenvname`
        <br>`conda install pip`
        <br>`pip install -r requirements.txt
    </p> 
</blockquote>
