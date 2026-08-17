#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, amount;

    cout << "Enter number of coins: ";
    cin >> n;

    vector<int> coins(n);

    cout << "Enter coin values: ";
    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    cout << "Enter amount: ";
    cin >> amount;

    vector<int> dp(amount + 1, 9999);

    dp[0] = 0;

    for (int i = 1; i <= amount; i++)
    {
        for (int coin : coins)
        {
            if (coin <= i)
            {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    if (dp[amount] == 9999)
        cout << "Amount cannot be formed.";
    else
        cout << "Minimum number of coins = " << dp[amount];

    return 0;
}
