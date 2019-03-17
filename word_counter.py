#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import io

def get_words():
    words = []
    if len(sys.argv) > 1:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, sys.argv[1])
        try:
            with io.open(file_path, 'r', encoding='utf8') as f:
               file_content = f.read()
        except IOError:
            print 'cannot open', sys.argv[1]
        else:       
            for word in file_content.lower().split():
                word.replace(".","")
                word.replace(",","")
                word.replace(":","")
                word.replace("\"","")
                word.replace("!","")
                word.replace("*","")
                word.replace(u"â€œ","")
                word.replace(u"â€˜","")
                words.append(word)  
            f.close()    
            return words
    else:
        return False
    
def count_words(words):
    return len(words)

def common_occurance(words):
    uniqWords=sorted(set(words))
    occurance={}
    for word in uniqWords:
        occurance[word] =  words.count(word)
    occurance = sorted(occurance.items(), key=lambda(k,v) : v, reverse=True)
    return occurance[:10]


if __name__ == '__main__':
    words = get_words()
    if words :
        print count_words(words)
        print common_occurance(words)
    else :
        print "File path doesn't exist"