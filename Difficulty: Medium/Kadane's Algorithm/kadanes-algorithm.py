#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        
        size = len(arr)
        dp = [0] * size
    
        # Initialize the first element of the list with the first element of the array
        dp[0] = arr[0]
    
        # Initialize the answer with the first element of the array
        ans = dp[0]
    
        # Loop through the array starting from the second element
        for i in range(1, size):
            # Choose the maximum value between the current element and the sum of the current element
            # and the previous maximum sum (stored in dp[i - 1])
            dp[i] = max(arr[i], arr[i] + dp[i - 1])
    
            # Update the overall maximum sum
            ans = max(ans, dp[i])
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends