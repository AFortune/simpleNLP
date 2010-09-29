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

def search_in_trie(chars, trie):
    ref=trie
    index=0
    for char in chars:
        if ref.has_key(char):
            #print char,
            ref=ref[char] 
            index+=1
        else:
            if index==0:
                index=1
            #    print char, 
            #print '*',
            try:
                chars=chars[index:]
                search_in_trie(chars, trie)
            except:
                pass
            break
def main():
    #init
    words=init_wordslist()
    trie=words_2_trie(words)
    #read content
    fn= sys.argv[1]
    lines=open(fn).readlines()
    index=1
    for line in lines:
        print "\nline %d:\n%s\n" % (index, "*" * 80 )
        chars=regex.findall(line) 
        #do the job
        search_in_trie(chars, trie)
        index += 1

if __name__=='__main__':
    main()

