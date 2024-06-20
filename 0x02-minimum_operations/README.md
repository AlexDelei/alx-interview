### Dynamic Programming
**Dynamic Programming** is a method used in mathematics and computer science to solve complex problems by breaking them down into simpler subproblems. By solving each subproblem only once and storing the results, it avoids redundant computations, leading to more efficient solutions for a wide range of problems.

### How Does dynamic programming work ?
1. **Identify Subproblems** - Divide the main problem into smaller, independent subproblems.
2. **Store Solutions** - Solve each problem and store the solution into an array.
3. **Build Up Solutions** - Use the stored solution to build up to the main problem.
4. **Avoids redudancy** - By storing solutions. computation time is reduced.

### When to use Dynamic Programming (DP) ?
Dynamic programming is an optimization technique used when solving problems that
consist of the following characteristics:

1. Optimal Substructure:

Optimal substructure means that we combine the optimal results of subproblems to achieve the optimal result of the bigger problem.

Example:

```Consider the problem of finding the minimum cost path in a weighted graph from a source node to a destination node. We can break this problem down into smaller subproblems:

- Find the minimum cost path from the source node to each intermediate node.
- Find the minimum cost path from each intermediate node to the destination node.
- The solution to the larger problem (finding the minimum cost path from the source node to the destination node) can be constructed from the solutions to these smaller subproblems.
```


2. Overlapping Subproblems

The same subproblems are solved repeatedly in different parts of the problem.

Example:

```Consider the problem of computing the Fibonacci series. To compute the Fibonacci number at index n, we need to compute the Fibonacci numbers at indices n-1 and n-2. This means that the subproblem of computing the Fibonacci number at index n-1 is used twice in the solution to the larger problem of computing the Fibonacci number at index n.```


### Advantages of Dynamic Programming (DP)
1. Avoids recomputing the same subproblem multiple times, leading to significant time savings.
2. Ensures that the optimal solution is found by considering all possible combinations.
3. Breaks down smaller problems into, smaller more manageble subproblems




#### Dynamic Programming (DP) Algorithm
**Dynamic programming** is a algorithmic technique that solves complex problems by breaking them down into smaller subproblems and storing their solutions for future use. It is particularly effective for problems that contains overlapping subproblems and optimal substructure.

Common Algorithms that Use Dynamic Programming:

1. Longest Common Subsequence (LCS): Finds the longest common subsequence between two strings.
2. Shortest Path in a Graph: Finds the shortest path between two nodes in a graph.
3. Knapsack Problem: Determines the maximum value of items that can be placed in a knapsack with a given capacity.
4. Matrix Chain Multiplication: Optimizes the order of matrix multiplication to minimize the number of operations.
5. Fibonacci Sequence: Calculates the nth Fibonacci number.



#### Explanation for ```minOperations()``` : Dynamic Programming.
Explaining like a five year child ->
```
#!/usr/bin/env python3
"""
Finding the minimum number of operations to perform
"""


def minOperations(n: int) -> int:
    """
    Calculating the minimum number of operations
    """
    if n == 0:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n]

```

#### How It Works

1. **Define the Problem:**

You want to know how many steps it takes to write 'a' n times.

2. **Special Case:**

If n is 0, it means you don't want to write any 'a', so it returns 0 steps.

3. **Setting Up a List:**

The code creates a list called dp to keep track of the smallest number of steps needed for each number from 0 to n.
It starts by assuming it takes a very large number of steps ```(float('inf'))``` for any number of 'a's. This just means we haven't figured out the real number of steps yet.
It knows that it takes 0 steps to have 1 'a' because you haven't done anything yet (this might be a point for clarification since in practice it takes 1 step to insert one 'a').
Filling Up the List:

The code then goes through each number from 1 to n to figure out how many steps it takes to get there.
For each number i, it checks all possible smaller numbers j that can divide i evenly.
If i can be divided by j ```(meaning i % j == 0)```, it means you can get i 'a's by first writing j 'a's and then pasting them enough times.

4. **Finding the Minimum Steps:**

For each i, it keeps track of the smallest number of steps needed by comparing the current number of steps ```(dp[i])``` with the steps needed to get to j plus the steps needed to paste j enough times to get i ```(which is (i // j)``` steps).

5. **Return the Result:**

After it figures out the smallest number of steps for each number up to n, it returns the number of steps for n ```(dp[n])```.
