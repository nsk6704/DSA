"""
Question : LC 73
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

"""

# Brute force solution

"""
Here, what we do is, we take the length of rows and cols, iterate over the matrix. When we we find a cell which has 0 , we mark all the cells in that row/col which are not 0 as -1. Finally we iterate back and mark the -1 cells back to 0.

However it is important to note that this kind of solution fails when -1 is itself in the array. To solve this issue we need to look at the Better Approach
"""

def setZeroes(self, matrix: List[List[int]]) -> None:
  n = len(matrix)
  m = len(matrix[0])

  for i in range(n):
    for j in range(m):

      if matrix[i][j] == 0:

        for k in range(n):
          if matrix[k][j] != 1:
            matrix[k][j] = -1

        for k in range(m):
          if matrix[i][k] != 1:
            matrix[i][k] = -1

  for i in range(n):
    for j in range(m):
      if matrix[i][j] = -1:
        matrix[i][j] = 0



# Better Approach

"""
Now, the better approach takes two additional arrays. Here we see if a cell is 0, and mark the entire row and col(i.e. store their indexes) by marking as 1. In the end we just iterate and if the cell is patrt of the col or row in our arrays, we mark it as 0.
"""


def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        marked_rows = [0] * rows
        marked_cols = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    marked_rows[row] = 1
                    marked_cols[col] = 1

        for row in range(rows):
            for col in range(cols):
                if (marked_rows[row] or marked_cols[col]):
                    matrix[row][col] = 0


# Optimal Approach 

"""
Here, we use the first row and column as the markers instead of creating 2 extra arrays, and handle the first row and the forst column replacement separately.
"""

def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero == True:
            for c in range(cols):
                matrix[0][c] = 0

  
