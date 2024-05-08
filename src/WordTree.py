import numpy as np
import sys,os
import re

treeMaxDist=5
# Freq is sentence use count
# {"hello":{"freq":1,"children":{ recursion }}}
Tree={}
def updateTree(tree: dict, path: list, loc: dict):
    if len(path)==0:
        return tree
    if path[0].lower() in tree:
        tree[path[0].lower()]["freq"]+=1
        if len(path)>1:
            tree=updateTree(tree[path[0]],path[1:],loc)
    else:
        tree[path[0].lower()]={"freq":1,"children":{}}
        if len(path)>1:
            tree=updateTree(tree[path[0]],path[1:],loc)
    return tree

def CompilerTree(orig: dict,sentences: list):
    tree=orig
    sentences=[[y.lower() for y in re.findall(r"(\w+| |.)", x) if y!=" "] for x in sentences]
    print(sentences)
    for words in sentences:
        path=[]
        for f in range(treeMaxDist-1,len(words)):
            for a in range(treeMaxDist):
                x=a+f-treeMaxDist+1
                loc=tree
                print("path:",path)
                parent={}
                for y in path:
                    parent=loc[y]
                    loc=loc[y]["children"]
                if words[x].lower() in loc:
                    loc[words[x].lower()]["freq"]+=1
                else:
                    loc[words[x].lower()]={"freq":1,"children":{}}
                path.append(words[x].lower())
                if len(path)>treeMaxDist:
                    path.pop(0)
                print("finished path",path)
                print("finished loc",loc)
                print("before tree update",tree)
                #tree=updateTree(tree,path,loc)
                print("after tree update",tree)
    return tree

print(CompilerTree(Tree,["This is a sentence.","This is another sentence.","Hello, world!"]))