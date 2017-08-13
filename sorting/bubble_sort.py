# created by Yunindyo Prabowo


# inisialisasi array
list_sorting = [10, 2, 5, 8, 1, 20, 7, 3, 4]

# method bubble sort


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                print(alist)


bubbleSort(list_sorting)
print()
print("---")
print(list_sorting)
print("---")
