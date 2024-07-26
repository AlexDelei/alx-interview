### 0. Change from within

**Pseudocode**
For each coin, there are 2 options.

Include the current coin: Subtract the current coin’s denomination from the target sum and call the count function recursively with the updated sum and the same set of coins i.e., count(coins, n, sum – coins[n-1] )
Exclude the current coin: Call the count function recursively with the same sum and the remaining coins. i.e., count(coins, n-1,sum ).
The final result will be the sum of both cases.

Base case:

If the target sum (sum) is 0, there is only one way to make the sum, which is by not selecting any coin. So, count(0, coins, n) = 1.
If the target sum (sum) is negative or no coins are left to consider (n == 0), then there are no ways to make the sum, so count(sum, coins, 0) = 0.