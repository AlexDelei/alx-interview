#### Rotating a 2D Matrix in python

_Pseudocode_
1. There are N/2 squares or cycles in a matrix of side N. Process a square one at a time. Run a loop to traverse the matrix a cycle at a time, i.e loop from 0 to N/2 – 1, loop counter is i
2. Consider elements in group of 4 in current square, rotate the 4 elements at a time. So the number of such groups in a cycle is N – 2*i.
3. So run a loop in each cycle from x to N – x – 1, loop counter is y
4. The elements in the current group is (x, y), (y, N-1-x), (N-1-x, N-1-y), (N-1-y, x), now rotate the these 4 elements, i.e (x, y) <- (y, N-1-x), (y, N-1-x)<- (N-1-x, N-1-y), (N-1-x, N-1-y)<- (N-1-y, x), (N-1-y, x)<- (x, y)
5. Print the matrix.