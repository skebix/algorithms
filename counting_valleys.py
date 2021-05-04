#!/bin/python3

import os


# HackerRank "Counting Valleys" from Interview Preparation Kit (Warm-up Challenges)
def counting_valleys(steps, path):
    altitude, valleys = 0, 0
    for step in path:
        altitude += 1 if step == 'U' else -1
        if altitude == 0 and step == 'U':
            valleys += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = counting_valleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
