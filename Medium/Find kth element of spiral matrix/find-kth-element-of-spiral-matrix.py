#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        left = 0
        right = m - 1
        up = 0
        down = n - 1
        count = 1

        while left <= right and up <= down:
            for i in range(left, right + 1):
                if count == k:
                    return a[up][i]
                count += 1
            up += 1

            for i in range(up, down + 1):
                if count == k:
                    return a[i][right]
                count += 1
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    if count == k:
                        return a[down][i]
                    count += 1
                down -= 1

            if left <= right:
                for i in range(down, up - 1, -1):
                    if count == k:
                        return a[i][left]
                    count += 1
                left += 1

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends