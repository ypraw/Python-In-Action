# SIMPLE TEST LIST CREATION
this scipt written when i stuck on my undergraduate thesis hahahaha , forget it ,it's .. ah just simpel test script using built in package timeit and third library numpy, so just install numpy using pip XD.


* built in 
  * list.insert()
  ```python
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
  ```

  * list.append()
    ```python
        def listappend(item):
            i=0
            mylist=[]
            while i<= item:
                mylist.append(i)
                i+=1
            return mylist
    ```
    
* list comprehension
```python
[x for x in range (1000)]
```

* Third library
  * numpy
    ```python
    def listnumpy(item):
        mylist=np.arange(item)
        return mylist

    ```
