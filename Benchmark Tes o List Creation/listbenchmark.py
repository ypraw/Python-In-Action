import timeit
from collections import OrderedDict
import numpy as np

number=5000


def backInsert(item):
    i=0
    mylist=[]
    while i<=item:
      mylist.insert(len(mylist),i)
      i+=1
    return mylist


def frontInsert(item):
    i=0
    mylist=[]
    while i<= item:
        mylist.insert(0,i)
        i+=1
    return mylist

def listappend(item):
    i=0
    mylist=[]
    while i<= item:
        mylist.append(i)
        i+=1
    return mylist

def listnumpy(item):
    mylist=np.arange(item)
    return mylist
#print(badInsert(1000))
#print(reverseListInsert(1000))

time1=timeit.timeit("backInsert(1000)",globals=globals(),number=number)
time2=timeit.timeit("frontInsert(1000)",globals=globals(),number=number)
time3=timeit.timeit("[x for x in range(1000)]",globals=globals(),number=number)
time4=timeit.timeit("listappend(1000)",globals=globals(),number=number)
time5=timeit.timeit("listnumpy(1000)",globals=globals(),number=number)
res=dict(back_insert=time1 ,front_insert=time2,list_compre=time3,list_append=time4,numpy_array=time5)
res=OrderedDict(sorted(res.items(),key=lambda x:x[1]))
print(f"LIST CREATION BENCHMARKING TEST\n*> every method generate 1000 items\n*> {number} loops for testing\n\n")
for k,v in res.items():
    print(f'{k} : {v:.5f} seconds')
#print(f'from back: {time1:.3f} \nfrom front: {time2:.3f} \nlist compre: {time3:.3f} \nappend: {time4:.3f} \nnumpy array: {time5:.3f}')