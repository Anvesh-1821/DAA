#include <iostream>
#include <ctime>
using namespace std;

// Iterative Factorial
long long factorialIterative(int n)
{
    long long result = 1;

    for (int i = 1; i <= n; i++)
        result = result * i;

    return result;
}

// Recursive Factorial
long long factorialRecursive(int n)
{
    if (n <= 1)
        return 1;

    return n * factorialRecursive(n - 1);
}

// Main Program
int main()
{
    int n;

    cout << "Enter a non-negative integer (e.g., 20): ";
    cin >> n;

    if (n < 0)
    {
        cout << "Invalid input! Please enter a non-negative integer.";
    }
    else
    {
        // Iterative Time
        clock_t start = clock();
        long long iterativeResult = factorialIterative(n);
        clock_t end = clock();

        double iterativeTime =
            (double)(end - start) * 1000000000 / CLOCKS_PER_SEC;

        // Recursive Time
        start = clock();
        long long recursiveResult = factorialRecursive(n);
        end = clock();

        double recursiveTime =
            (double)(end - start) * 1000000000 / CLOCKS_PER_SEC;

        // Display Results
        cout << "\n--- Results for " << n << "! ---\n";

        cout << "Iterative Result : " << iterativeResult << endl;
        cout << "Iterative Time   : " << iterativeTime << " ns" << endl;

        cout << "-------------------------------\n";

        cout << "Recursive Result : " << recursiveResult << endl;
        cout << "Recursive Time   : " << recursiveTime << " ns" << endl;
    }

    return 0;
}
