def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def linear_search(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


arr = [10, 20, 30, 40, 50]

# Binary Search
key1 = 40
result1 = binary_search(arr, key1)
print("Binary Search: Element found at index", result1)

# Linear Search
key2 = 20
n = len(arr)
result2 = linear_search(arr, n, key2)
print("Linear Search: Element found at index", result2)
