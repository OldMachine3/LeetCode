class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tampung = 0
        n = len(grid[0])

        for row in grid:
            left, right = 0, n-1
            while left <= right:
                mid = (right + left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
                
            tampung += (n - left)

        return tampung
