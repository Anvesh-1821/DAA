#include <iostream>
#include <vector>
using namespace std;

// Bubble Sort
void bubbleSort(vector<int>& a) {
    for (int i = 0; i < a.size() - 1; i++)
        for (int j = 0; j < a.size() - i - 1; j++)
            if (a[j] > a[j + 1])
                swap(a[j], a[j + 1]);
}

// Selection Sort
void selectionSort(vector<int>& a) {
    for (int i = 0; i < a.size() - 1; i++) {
        int min = i;

        for (int j = i + 1; j < a.size(); j++)
            if (a[j] < a[min])
                min = j;

        swap(a[i], a[min]);
    }
}

// Insertion Sort
void insertionSort(vector<int>& a) {
    for (int i = 1; i < a.size(); i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }
}

// Merge Sort
void mergeSort(vector<int>& a, int left, int right) {
    if (left >= right)
        return;

    int mid = (left + right) / 2;

    mergeSort(a, left, mid);
    mergeSort(a, mid + 1, right);

    vector<int> temp;
    int i = left, j = mid + 1;

    while (i <= mid && j <= right) {
        if (a[i] <= a[j])
            temp.push_back(a[i++]);
        else
            temp.push_back(a[j++]);
    }

    while (i <= mid)
        temp.push_back(a[i++]);

    while (j <= right)
        temp.push_back(a[j++]);

    for (int k = 0; k < temp.size(); k++)
        a[left + k] = temp[k];
}

// Quick Sort
void quickSort(vector<int>& a, int low, int high) {
    if (low >= high)
        return;

    int pivot = a[high];
    int i = low;

    for (int j = low; j < high; j++) {
        if (a[j] < pivot)
            swap(a[i++], a[j]);
    }

    swap(a[i], a[high]);

    quickSort(a, low, i - 1);
    quickSort(a, i + 1, high);
}

int main() {
    vector<int> a = {64, 25, 12, 22, 11};

    cout << "Original Array: ";
    for (int x : a)
        cout << x << " ";

    cout << "\n\n";

    vector<int> b;

    b = a;
    bubbleSort(b);
    cout << "Bubble Sort: ";
    for (int x : b) cout << x << " ";

    b = a;
    selectionSort(b);
    cout << "\nSelection Sort: ";
    for (int x : b) cout << x << " ";

    b = a;
    insertionSort(b);
    cout << "\nInsertion Sort: ";
    for (int x : b) cout << x << " ";

    b = a;
    mergeSort(b, 0, b.size() - 1);
    cout << "\nMerge Sort: ";
    for (int x : b) cout << x << " ";

    b = a;
    quickSort(b, 0, b.size() - 1);
    cout << "\nQuick Sort: ";
    for (int x : b) cout << x << " ";

    return 0;
}
