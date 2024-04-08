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

def colorize(text,cpos=0):
	txt=text
	#txt=txt[:cpos+1]+chr(21)+txt[cpos+1:]
	print(cpos)
	print("--",len(text))
	print("--",txt[:cpos]+chr(21)+txt[cpos:])
	t=[]#word_tokenize(txt)
	print(t)
	tagged=pos_tag(t)
	out=txt
	#print("->",out)
	before=""
	for n,i in zip(range(len(tagged)),tagged):
		if i[0].__contains__(chr(21)):
			before=out[:out.find(i[0])]
			out=out.replace(i[0], chr(21))
			out=out[out.find(chr(21))+1-len(i[0]):]
			continue
		if i[1].startswith('NN') or i[1].startswith('VB') or i[1].startswith('JJ'):
			print("Matched",i[0],out.find(i[0]))
			out=out.replace(i[0], rgb_txt(i[0], [0, 0, 30]),1)
			print("2",out)
	print(before)
	print(out)
	return (before,out)

print(chr(21))
colorize("test",2)