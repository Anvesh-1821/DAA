#include <iostream>
#include <ctime>
using namespace std;

// Linear Search
int linearSearch(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

// Binary Search
int binarySearch(int arr[], int n, int key)
{
    int low = 0;
    int high = n - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}

// Main Program
int main()
{
    int n = 50000;
    int arr[50000];

    // Create sorted array
    for (int i = 0; i < n; i++)
        arr[i] = i + 1;

    int key;
    cout << "Enter element to search: ";
    cin >> key;

    // Linear Search Timing
    clock_t start = clock();
    int index = linearSearch(arr, n, key);
    clock_t end = clock();

    double linearTime =
        (double)(end - start) * 1000000 / CLOCKS_PER_SEC;

    cout << "\nLinear Search" << endl;
    if (index != -1)
        cout << "Element found at index: " << index << endl;
    else
        cout << "Element not found" << endl;

    cout << "Time Taken: " << linearTime << " microseconds" << endl;

    // Binary Search Timing
    start = clock();
    index = binarySearch(arr, n, key);
    end = clock();

    double binaryTime =
        (double)(end - start) * 1000000 / CLOCKS_PER_SEC;

    cout << "\nBinary Search" << endl;
    if (index != -1)
        cout << "Element found at index: " << index << endl;
    else
        cout << "Element not found" << endl;

    cout << "Time Taken: " << binaryTime << " microseconds" << endl;

    return 0;
}
