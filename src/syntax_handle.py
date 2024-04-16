import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer as TWD
from nltk import pos_tag
from html import escape
import nltk
#from GUI import rgb_txt,css_txt



def rgb_txt(text,rgb):
	return "<span style='color:rgb({R},{G},{B});display:inline-block;white-space: pre;'>{txt}</span>".format(R=rgb[0],G=rgb[1],B=rgb[2],txt=escape(text))
def css_txt(text,css):
	return "<span style='{css}'>{txt}</span>".format(css=css,txt=escape(text))
def rl(x):
	return range(len(x))

def colorize(text,cpos=0):
	offset=text.count("\t")*3
	txt=text.replace("\t","    ")
	if len(txt)==0:
		return (txt,0)
	#txt=txt[:cpos]+chr(21)+txt[cpos:]
	words=word_tokenize(txt)
	tags=pos_tag(words)
	if len(tags)==0 or len(words)==0:
		return (rgb_txt(txt,(200,200,200)),offset)
	before=txt[:txt.find(tags[0][0])]
	pullfrom=txt
	out=""
	for i in rl(tags):
		find=pullfrom.find(tags[i][0])+len(tags[i][0])
		color=(200,200,200)
		m=tags[i][1][:2]
		if m=="NN":
			color=(200,255,200)
		elif m=="VB":
			color=(255,200,200)
		elif m=="JJ":
			color=(200,200,255)
		elif m=="." or m=="!" or m=="?":
			color=(255,127,0)
		else:
			color=(200,200,200)
		out+=rgb_txt(pullfrom[:find], color)
		pullfrom=pullfrom[find:]
	#print("==",[pre+WorkingOn],[post])
	return (out+pullfrom,offset)