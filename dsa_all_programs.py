# 1. Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 2. Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 3. Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


# 4. Merge Sort

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# 5. Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# 6. Heap Sort

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# 7. Counting Sort

def counting_sort(arr):
    if len(arr) == 0:
        return arr

    maximum = max(arr)
    count = [0] * (maximum + 1)

    for num in arr:
        count[num] += 1

    result = []

    for i in range(len(count)):
        while count[i] > 0:
            result.append(i)
            count[i] -= 1

    return result


# 8. Hash Functions

def division_hash(key, size):
    return key % size


def mid_square_hash(key, size):
    square = key * key
    middle = (square // 10) % 100
    return middle % size


def folding_hash(key, size):
    string = str(key)
    total = 0

    for i in range(0, len(string), 2):
        total += int(string[i:i + 2])

    return total % size


# 9. Hashing - Chaining

class HashChaining:

    def _init_(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# 10. Hashing - Linear Probing

class HashLinearProbing:

    def _init_(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            index = (index + 1) % self.size

            if index == start:
                print("Hash table is full")
                return

        self.table[index] = key

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return True

            index = (index + 1) % self.size

            if index == start:
                break

        return False

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# MAIN PROGRAM

data = [64, 25, 12, 22, 11]

print("Bubble Sort:", bubble_sort(data.copy()))
print("Selection Sort:", selection_sort(data.copy()))
print("Insertion Sort:", insertion_sort(data.copy()))

data = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort:", merge_sort(data))

data = [10, 7, 8, 9, 1, 5]
print("Quick Sort:", quick_sort(data))

data = [12, 11, 13, 5, 6, 7]
print("Heap Sort:", heap_sort(data))

data = [4, 2, 2, 8, 3 , 1]