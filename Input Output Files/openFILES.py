####################################
##  open and Writing files using  ##
## Regular Expression             ##
####################################

import re


def openFILE(dirFile):
    f = open(dirFile, 'r')
    return f.read()


def readFILES(dirFile):
    # replace with a directory of files that you want to open
    result = openFILE("f:\Python\Practice\coba.txt")
    Replace = re.findall(r'\d+\.*\d*',
                         result)  # find value only floating data types
    # tes=0
    file = open(dirFile, 'w')
    for item in Replace:
        item = int(round(
            float(item)))  # this example for parsing string to int
        # tes=int (tes+item)
        # print( tes )

        item = str(item)  # make sure for writing files data types is string
        file.write(item + "\n")
        print(item)
    file.close()


# CALL METHOD
readFILES("f:\Python\Practice\Files.txt"
          )  # replace with a directory of files that you want to save
