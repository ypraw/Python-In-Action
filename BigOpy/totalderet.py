import timeit

def totalderet1(sizeData):
    total=0
    for value in range(1,sizeData+1):
        total+=value
    return total


def totalderet2(sizeData):
    return (sizeData *(sizeData+1))/2

size=10

print(f'total {size} bilangan adalah dengan loop {totalderet1(size)}') 
print(f'total {size} bilangan adalah dengan fungsi matematika {totalderet2(size)}') 

""" Testing """
number=1000
time1 = timeit.timeit("totalderet1(size)",globals=globals(),number=number)
time2 = timeit.timeit("totalderet2(size)",globals=globals(),number=number)

print(f'timer dengan looop {time1:.5f}\ntime dengan math {time2:.5f}')