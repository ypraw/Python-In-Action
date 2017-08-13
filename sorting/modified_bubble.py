def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                print(alist)
        passnum = passnum - 1


alist = [10, 2, 5, 8, 1, 20, 7, 3, 4]
shortBubbleSort(alist)
print(alist)
