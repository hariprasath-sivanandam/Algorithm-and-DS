Question:

https://leetcode.com/problems/perfect-squares/description/

Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

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