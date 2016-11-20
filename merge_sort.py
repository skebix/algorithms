import random, time


def merge_sort(a):
    """
    Sort an array recursively by sorting its halves
    """
    n = len(a)
    if n == 0 or n == 1:
        return a

    middle = n // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])

    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays in a resulting array of size len(left) + len(right)
    """

    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) == 0:
        result += right
    else:
        result += left

    return result


l = random.sample(range(1, 1000001), 100000)

print(l)

start_time = time.time()
l = merge_sort(l)
print("%s seconds" % (time.time() - start_time))

print(l)
