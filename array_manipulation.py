#!/bin/python3

import os


# HackerRank "Array Manipulation" from Interview Preparation Kit
def array_manipulation(n, m, queries):
    """The magic here is keep track of max while adding from left to right in the second loop"""
    arr = [0] * (n + 1)
    maximum = 0
    for i in range(m):
        arr[queries[i][0]] += queries[i][2]
        if queries[i][1] + 1 <= n:
            arr[queries[i][1] + 1] -= queries[i][2]
    added = 0
    for e in arr:
        added += e
        if added > maximum:
            maximum = added
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

