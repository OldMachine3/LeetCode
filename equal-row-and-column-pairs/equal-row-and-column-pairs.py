class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(grid)


        for r in range(n):
            for c in range(n):
                match = True

                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break
                count += int(match)
        return count