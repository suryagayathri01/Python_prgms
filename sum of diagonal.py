import math
import os
import random
import re
import sys


def DIAGONAL_SUM(n, A):
    sum_l=0;sum_r=0
    for i in range(n):
        for j in range(n):
            if i==j:
                sum_l+=A[i][j]
            if i+j== n-1:
                sum_r+=A[i][j]
    return sum_l, sum_r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = []

    for _ in range(n):
        A.append(list(map(int, input().rstrip().split())))

    slrd = DIAGONAL_SUM(n, A)

    fptr.write(' '.join(map(str, slrd)))
    fptr.write('\n')

    fptr.close()