import random, time


def linear_search(a, v):
    """Linear search algorithm. If v exist in a, returns index. Returns None if not found."""

    index = 0

    while index < len(a):
        if a[index] == v:
            return index
        index += 1

    return None


l = random.sample(range(1, 10000000), 1000000)

start_time = time.time()
i = linear_search(l, l[999999])
j = linear_search(l, -1)
print("%s seconds" % (time.time() - start_time))

print("Element is in position %s" % i)
print("Element is in position %s" % j)
