Question:

https://leetcode.com/problems/maximum-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.


Solution:

class Solution {
    public int numSquares(int n) {
        
        int dp[] = new int[n+1];
        dp[0] = 0;
        dp[1] =1;       
        
        for(int i=2;i<n+1;i++){
            dp[i]=Integer.MAX_VALUE;
            for(int j=1;(j*j)<=n;j++)
                if(i-(j*j) >=0)
                    dp[i] = Math.min(dp[i], dp[i-(j*j)]+1);
        }
        return dp[n];
    }
}