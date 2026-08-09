import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr, low, high):

    if low < high:

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        pi = i + 1

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Main Program
n = 100

arr = [random.randint(0, 999) for _ in range(n)]

print("Number of Elements =", n)
print()


# Bubble Sort
temp = arr.copy()
start = time.time()

bubble_sort(temp)

end = time.time()
print("Bubble Sort Time    :", (end - start) * 1000000, "microseconds")


# Selection Sort
temp = arr.copy()
start = time.time()

selection_sort(temp)

end = time.time()
print("Selection Sort Time :", (end - start) * 1000000, "microseconds")

# Insertion Sort
temp = arr.copy()
start = time.time()

insertion_sort(temp)

end = time.time()
print("Insertion Sort Time :", (end - start) * 1000000, "microseconds")

# Merge Sort
temp = arr.copy()
start = time.time()

merge_sort(temp)

end = time.time()
print("Merge Sort Time     :", (end - start) * 1000000, "microseconds")

# Quick Sort
temp = arr.copy()
start = time.time()

quick_sort(temp, 0, n - 1)

end = time.time()
print("Quick Sort Time     :", (end - start) * 1000000, "microseconds")
