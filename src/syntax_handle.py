import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer as TWD
from nltk import pos_tag
from html import escape
import nltk
#from GUI import rgb_txt,css_txt



def rgb_txt(text,rgb):
	return "<span style='color:rgb({R},{G},{B})'>{txt}</span>".format(R=rgb[0],G=rgb[1],B=rgb[2],txt=escape(text))
def css_txt(text,css):
	return "<span style='{css}'>{txt}</span>".format(css=css,txt=escape(text))
def rl(x):
	return range(len(x))

def color_list(l):
	out=[]
	for x in l:
		color=(200,200,200)
		match x[1]:
			case "NN":
				color=(200,200,255)
			case "VB":
				color=(255,200,200)
			case "JJ":
				color=(200,255,200)
			case _:
				color=(200,200,200)
		out.append(rgb_txt(x[0],color))
	print("cl-",l,TWD().detokenize(out))
	return TWD().detokenize(out)

def colorize(text,cpos=0):
	txt=text
	txt=txt[:cpos]+chr(21)+txt[cpos:]
	if txt=="\x15":
		return ("","","")
	print(cpos)
	print(txt)
	lines=txt.split("\n")
	# t=word_tokenize(txt)
	t=[]
	for x in rl(lines):
		print("--",lines[x])
		t+=word_tokenize(lines[x])
		print(t)
		if x!=len(lines)-1:
			t.append("\n")
	if t.__contains__("\x15"):
		t[t.index("\x15")]=" \x15"
	WorkingOn=""
	WorkingOnIndex=0
	PreT=[]
	PostT=[]
	for i in range(len(t)):
		if t[i].__contains__(chr(21)):
			PreT=t[:i+1]
			WorkingOn=t[i]
			WorkingOnIndex=i
			PostT=t[i+1:]
			break
	pre=""
	post=""
	if len(PreT)==0:
		pre=""
	else:
		preToken=pos_tag(PreT)
		pre=color_list(preToken)
	if len(PostT)==0:
		post=""
	else:
		postToken=pos_tag(PostT)
		post=color_list(postToken)
	WorkingOn=WorkingOn.replace("\x15","")
	print("==",[pre+WorkingOn],[post])
	return [pre,WorkingOn,post]