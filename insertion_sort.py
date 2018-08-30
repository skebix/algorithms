import random, time


def insertion_sort(a):
    """Insertion sort algorithm. Take A[j], and insert it in the sorted sequence A[0..j-1]
    In any given iteration, A[0..j-1] is sorted and A[j+1..n] are the elements to be sorted"""
    for i in range(1, len(a)):
        j = i
        while(j > 0 and l[j] < l[j - 1]):
        	l[j], l[j - 1] = l[j - 1], l[j]
        	j -= 1


l = random.sample(range(1, 1000001), 10000)

print(l)

start_time = time.time()
insertion_sort(l)
print("%s seconds" % (time.time() - start_time))

print(l)