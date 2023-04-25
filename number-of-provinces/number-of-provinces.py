class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()  # Initialize visited set
        
        # Define depth-first search (dfs) function
        def dfs(isConnected, visited, i):
            if i in visited:  # If already visited, return 0
                return 0
            visited.add(i)  # Add i to visited set
            for j in range(len(isConnected[i])):  # Check for direct connections
                if isConnected[i][j] == 1:
                    dfs(isConnected, visited, j)  # Recursively call dfs on j
            return 1  # Return 1 to represent current province
        
        provinces = 0  # Initialize provinces count
        for i in range(len(isConnected)):  # Loop through all cities
            provinces += dfs(isConnected, visited, i)  # Call dfs on city i and add result to provinces
        return provinces  # Return total number of provinces