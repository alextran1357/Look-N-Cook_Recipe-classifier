# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:55:03 2020

@author: Alex

This code will be to take a URL and extract the words from it
"""
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

url = "https://www.delish.com/cooking/recipe-ideas/recipes/a51337/classic-lasagna-recipe/"
html = urllib.request.urlopen(url).read()
temp = text_from_html(html)
templist = temp.split(":")

for i in range (len(templist)):
    templist[i] = " ".join(templist[i].split())

for i in range (len(templist)):
    print(templist[i])
    print('----------------------------------------------------------')
    