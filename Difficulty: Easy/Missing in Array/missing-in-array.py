#User function Template for python3
#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        l = len(arr)+1
        sumarr = sum(arr)
        expsum = l*(l+1)//2
        return (expsum-sumarr)# code here




#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends