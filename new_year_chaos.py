#!/bin/python3


# HackerRank "New Year Chaos" from Interview Preparation Kit
def minimum_bribes(queue):
    bribed = 0
    for current, original in enumerate(queue):
        if original - (current + 1) > 2:
            print("Too chaotic")
            return
        # If someone is ahead of current position, but is greater, it bribed current
        for j in range(max(original - 2, 0), current):
            if queue[j] > original:
                bribed += 1
    print(bribed)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
