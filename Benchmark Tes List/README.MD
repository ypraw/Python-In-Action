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

### Result

```bash
LIST CREATION BENCHMARKING TEST
*> every method generate 1000 items
*> 5000 loops for testing

numpy_array : 0.06775 seconds
list_compre : 1.53685 seconds
list_append : 5.75628 seconds
back_insert : 11.95435 seconds
front_insert : 19.08289 seconds
```
    
> this result came from my android , maybe different depend on your device, and any code written without any scientific methods or computer science methods, just random idea XD
