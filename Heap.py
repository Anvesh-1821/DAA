import random
import time


# ---------- MAX HEAP ----------
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def max_heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)5

    # Sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)


# ---------- MIN HEAP ----------
def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def min_heap_sort(arr):
    n = len(arr)

    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # Sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)

    # Reverse for ascending order
    arr.reverse()


# ---------- MAIN ----------
n = int(input("Enter number of elements: "))

original = [random.randint(0, 99999) for _ in range(n)]

max_heap_array = original.copy()
min_heap_array = original.copy()


# MAX HEAP SORT
start = time.perf_counter()
max_heap_sort(max_heap_array)
end = time.perf_counter()
max_time = end - start


# MIN HEAP SORT
start = time.perf_counter()
min_heap_sort(min_heap_array)
end = time.perf_counter()
min_time = end - start


print("\nOriginal Array:", original)
print("\nSorted using Max Heap:", max_heap_array)
print("Time:", round(max_time, 6), "seconds")

print("\nSorted using Min Heap:", min_heap_array)
print("Time:", round(min_time, 6), "seconds")
