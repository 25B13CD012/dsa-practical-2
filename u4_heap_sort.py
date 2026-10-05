def heapify(a, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def build_max_heap(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)


def heap_sort(a):
    build_max_heap(a)
    print("Max-heap:", a)

    for end in range(len(a) - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)

    return a


data = [4, 10, 3, 5, 1, 8]

print("Input :", data)
print("Sorted :", heap_sort(data[:]))
