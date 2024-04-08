import re
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer as TWD
from nltk import pos_tag
from html import escape
import nltk
#from GUI import rgb_txt,css_txt
def rgb_txt(text,rgb):
	return "<span style='color:rgb({R},{G},{B})'>{txt}</span>".format(R=rgb[0],G=rgb[1],B=rgb[2],txt=escape(text))
def css_txt(text,css):
	return "<span style='{css}'>{txt}</span>".format(css=css,txt=escape(text))

def test(text):
	t=word_tokenize(text)
	print(t)
	tagged=pos_tag(t)
	l=text
	out=[]
	for x in tagged:
		if x[1].startswith("NN"):
			out.append(rgb_txt(x[0],[255,0,0]))
		elif x[1].startswith("VB"):
			out.append(rgb_txt(x[0],[0,255,0]))
		elif x[1].startswith("JJ"):
			out.append(rgb_txt(x[0],[0,0,255]))
		else:
			out.append(x[0])
	dt=TWD().detokenize(out)
	return dt