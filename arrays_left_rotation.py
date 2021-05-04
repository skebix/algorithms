#!/bin/python3

import os


# HackerRank "Arrays: Left Rotation" from Interview Preparation Kit
def left_rotation(li, rotations):
    return li[rotations:] + li[:rotations]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = left_rotation(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()