import time


def count_inversions(a):
    """
    Count left and right inversions recursively, piggybacking on merge sort
    """
    n = len(a)
    if n == 0 or n == 1:
        return a, 0

    middle = n // 2
    left, x = count_inversions(a[:middle])
    right, y = count_inversions(a[middle:])
    ordered, z = split_inversions(left, right)

    return ordered, x + y + z


def split_inversions(left, right):
    """
    Count the number of inversions where i <= n // 2 <= j, and a[i] > a[j]
    """
    total = 0
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            total += len(left)

    if len(left) == 0:
        result += right
    else:
        result += left

    return result, total


with open("count_inversion_test.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(int(line.strip()))


start_time = time.time()
l, t = count_inversions(array)
print("%s seconds" % (time.time() - start_time))

print(t)
