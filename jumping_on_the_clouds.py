#!/bin/python3

import os

# HackerRank "Jumping on the Clouds" from Interview Preparation Kit (Warm-up Challenges)
def jumping_on_clouds(clouds, number_of_clouds):
    jumps, lookahead = 0, 0
    while lookahead < number_of_clouds - 1:
        if clouds[lookahead] == 0:
            lookahead += 1
        lookahead += 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
