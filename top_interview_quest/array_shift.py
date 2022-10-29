import numpy as np


# class Solution(object):
#     def shiftGrid(self, grid, k):
#         """
#         :type grid: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
        
#         grid = np.matrix(grid)
#         a,b = grid.shape
       
#         grid = grid.flatten()
        
#         for i in range(k):
#             last = grid[0,-1]
#             for j in range(grid.shape[1] -1):
#                 grid[0, j+1] = grid[0,j]
#             grid[0,0] = last
#         grid.reshape(a,b)
#         print(grid)
        

# a = Solution()
# grid = [[1,2,3],[4,5,6],[7,8,9]]
# a.shiftGrid(grid, 1)

grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = np.array(grid)

a,b = grid.shape
k = 3
grid = grid.flatten()


for i in range(k):
    grid_new = np.copy(grid)
    # grid_new = grid_new.flatten()
    last = grid[-1]
    for j in range(grid.shape[0] -1):
        grid[j+1] = grid_new[j]
    grid[0] = last
grid = np.array(grid)
H = grid.reshape(a,b)
print(H)