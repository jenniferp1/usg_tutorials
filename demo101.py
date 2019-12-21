# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:56:39 2017

@author: JP
"""

def print_message(line,n=1):
    '''
    line = a string containing message to print to screen
    n = an integer telling the code how many times to print the message
    '''
    
    for i in range(n):
        print(line)
    
    return

def calc_area(w,l):
    '''
    w = width
    l = length
    Returns an area
    '''
    
    area = w * l
    
    return area

def calc_vol(area,h):
    '''
    area = area returned by cal_area
    h = height
    Returns a volume
    '''
    
    vol = area * h
    
    return vol