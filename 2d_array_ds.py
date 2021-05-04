#!/bin/python3

import math
import os


# HackerRank "2D Array - DS" from Interview Preparation Kit
def hourglass_sum(arr):
    max_hourglass = -math.inf
    for i in range(4):
        for j in range(4):
            current_hourglass = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + \
                                arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if current_hourglass > max_hourglass:
                max_hourglass = current_hourglass
    return max_hourglass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = []

    for _ in range(6):
        l.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(l)

    fptr.write(str(result) + '\n')

    fptr.close()
