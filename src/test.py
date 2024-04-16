from time import time
import numpy as np

def rl(x):
    return range(len(x))

def raw(a,b):
    a=" "+a
    b=" "+b
    arr=np.zeros((len(a),len(b)),dtype=int)
    arr[:,:]=99
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            if y==0:
                arr[0,x]=x
                continue
            if x==0:
                arr[y,0]=y
                continue
            arr[y,x]=min(arr[y-1:y+1,x-1:x+1].flatten())+min(abs(ord(a[y])-ord(b[x])),1)
    print(arr)
    return arr[-1,-1]
start=time()
print(raw("flight","knight"))
print("Time",(time()-start)*1000)