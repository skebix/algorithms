#!/bin/python3

import os


# HackerRank "Sales by Match" from Interview Preparation Kit (Warm-up Challenges)
def sock_merchant(n, ar):
    socks = {}
    pairs = 0
    for sock in ar:
        if sock not in socks:
            socks[sock] = sock
        else:
            pairs += 1
            del socks[sock]
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
