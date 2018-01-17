# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:00:29 2018

@author: 许晴雯
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


#def isCommon(ngram):
#    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
#    for word in ngram:
#        if word in commonWords:
#            return True
#    return False

def NonCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    NonCommon = []
    for word in ngram:
        if word not in commonWords:
            NonCommon.append(word)
    return NonCommon

def cleanInput(input):
    #re.sub()是替换的函数
    input = re.sub('\n+', " ",input).lower()
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +'," ",input)
    input = re.sub("u\.s\.", "us", input)
    input = bytes(input,"UTF-8")
    input = input.decode("ascii","ignore")
    cleanInput = []
    input = input.split(" ")
    for item in input :
        item = item.strip(string.punctuation)
        #去掉那些a,i,或者只有一个字母的单词
        if len(item) > 1 or (item.lower()=="a" or item.lower() == "i"):
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] +=1
    return output

def connent_string(NonCommon):
    connent_string = ""
    for word in NonCommon:
        connent_string = connent_string +" " + word
    return connent_string

def get_sentence(content):
    split_content = content.split(".")
    split_content = split_content.remove(" ")
#    for very_single_sent in split_content:
#        if "united states" in very_single_sent:    
#            return very_single_sent
    return print("Done.")

    
content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
#原始文章的长度
len_content = len(content)
len_content
#清理空格单字母后的文章长度
len_cleanInput = len(cleanInput(content))
len_cleanInput
#清理常用单词后的文章长度
len_NonCommon = len(NonCommon(cleanInput(content)))
len_NonCommon
#将清理常用单词后的文章连接起来，得到一篇简约的文章
content_NonCommon = connent_string(NonCommon(cleanInput(content)))

#ngrams = ngrams(content,2)
#
#ngrams = ngrams(content_NonCommon,2)
#
#sortedNGrams = sorted(ngrams.items(), key= operator.itemgetter(1),reverse = True)
#
#print(sortedNGrams)
#取出原文章中的句子
sentences = get_sentence(content)
print (sentences)
#计算一共有多少句子



        
        
        
        
        
        
        
        
        
        
    
    
