import random, time


def insertion_sort(a):
    """Insertion sort algorithm. Take A[j], and insert it in the sorted sequence A[0..j-1]
    In any given iteration, A[0..j-1] is sorted and A[j+1..n] are the elements to be sorted"""

    for j in range(1, len(a)):
        current = a[j]

        i = j - 1
        while i >= 0 and a[i] > current:
            a[i + 1] = a[i]
            i -= 1

        a[i + 1] = current


l = random.sample(range(1, 1000001), 10000)

print(l)

start_time = time.time()
insertion_sort(l)
print("%s seconds" % (time.time() - start_time))

print(l)
