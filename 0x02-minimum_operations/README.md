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
