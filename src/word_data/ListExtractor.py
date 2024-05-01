import os
f=open("FreqList.csv")
lines=f.readlines()
f.close()
new=[]
for x in lines:
	new.append(x.split(",")[0])
print(new)
f=open("FreqList.csv","w")
f.write("\n".join(new))
f.close()