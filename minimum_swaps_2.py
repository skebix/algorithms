#!/bin/python3

import os


# HackerRank "Minimum Swaps 2" from Interview Preparation Kit
def minimum_swaps(li):
    length = len(li)
    swaps = 0
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            swaps += 1
            li[min_index], li[i] = li[i], li[min_index]
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
