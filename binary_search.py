import math
import os
import random
import re
import sys

def BIN_SEARCH(n, arr, key):
    le=0;ri=n-1
    while le<=ri:
            mid= (le+ri)//2
            if key==arr[mid]:
                return mid
            elif key<arr[mid]:
                ri=mid-1
            elif key>arr[mid]:
                le=mid+1
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    idx = BIN_SEARCH(n, arr, k)

    fptr.write(str(idx) + '\n')

    fptr.close()
