#!/bin/python3

import os


# HackerRank "Repeated String" from Interview Preparation Kit (Warm-up Challenges)
def repeated_string(s, n):
    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
