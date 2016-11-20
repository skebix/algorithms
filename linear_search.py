import random, time


def linear_search(a, v):
    """Linear search algorithm. If v exist in a, returns index. Returns None if not found."""

    for index, e in enumerate(a):
        if e == v:
            return index
    return None

start_time = time.time()
l = random.sample(range(1, 100000001), 10000000)


i = linear_search(l, l[9999999])
j = linear_search(l, 1)
print("%s seconds" % (time.time() - start_time))

print("Element is in position %s" % i)
print("Element is in position %s" % j)
