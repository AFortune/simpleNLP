#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        x.py
#created:        2010-09-26 19:15

import re
import sys


regex=re.compile(r"(?x) (?: [\w-]+  | [\x80-\xff]{3} )")

def init_wordslist(fn="./words.txt"):
    f=open(fn)
    lines=sorted(f.readlines())
    f.close()
    return lines

def words_2_trie(wordslist):
    d={}
    for word in wordslist: 
        ref=d
        chars=regex.findall(word)
        for char in chars:
            ref[char]=ref.has_key(char) and ref[char] or {}
            ref=ref[char]
        ref['']=1
    return d
DEBUG=1

def search_in_trie(chars, trie): 
    print 
    while len(chars)>=1:
        ref=trie
        index=0
        state=[]
        for char in chars:
            if ref.has_key(char):
#                print char, 'h'
                if ref[char].has_key(""):
#                    print char,'e'
                    state.append(index)
                    #ref=trie
                    #break
                    ref=ref[char]
            else:
#                print char, 'nk'
                break
            index += 1
        if not state or state[-1]==0:
            index=1
            print chars[0],"*",
            chars=chars[1:]
        else:
            index=state[-1]+1
            print ''.join(chars[:index]), "*",
            chars=chars[index:]
        
           
def main():
    #init
    words=init_wordslist()
    i=0
    trie=words_2_trie(words)
    #read content
    fn= sys.argv[1]
    lines=open(fn).readlines()
    index=1
    for line in lines:
    
        chars=regex.findall(line) 
        search_in_trie(chars, trie)
        index += 1

if __name__=='__main__':
    main()

