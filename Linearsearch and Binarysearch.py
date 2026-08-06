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


# Main Program
arr = [10, 20, 30, 40, 50]

# Binary Search
key1 = 40
result1 = binary_search(arr, key1)

if result1 != -1:
    print("Binary Search: Element found at index", result1)
else:
    print("Binary Search: Element not found")

print("Time Complexity of Binary Search:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")
print("Space Complexity: O(1)\n")


# Linear Search
key2 = 20
n = len(arr)
result2 = linear_search(arr, n, key2)

if result2 != -1:
    print("Linear Search: Element found at index", result2)
else:
    print("Linear Search: Element not found")

print("Time Complexity of Linear Search:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")
print("Space Complexity: O(1)")
