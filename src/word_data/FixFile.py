import re
f=open("wordbank.txt","r")
words=f.readlines()
f.close()
f=open("wordbank.txt","w")
txt=""
for word in words:
	print(word.lower().strip())
	if re.search(r"[^a-z]",word.lower().strip())==None:
		txt+=word.lower()
f.write(txt)
f.close()