#User function Template for python3
from collections import deque

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		n = len(A)
		freq = [0] * 26
		q = deque()
		res = []
		for i in range(n):
		    freq[ord(A[i]) - ord('a')] += 1
		    q.append(A[i])
		    
		    while q:
		        if freq[ord(q[0]) - ord('a')] > 1:
		            q.popleft()
		        else:
		            res.append(q[0])
		            break
		    if not q:
		        res.append('#')
		 
		return ''.join(res)
            

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends