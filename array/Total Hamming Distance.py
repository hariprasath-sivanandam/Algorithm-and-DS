"""
Question:

https://leetcode.com/problems/total-hamming-distance/description/
477. Total Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

Solution:
"""

class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=[0 for _ in range(32)]
        for i in nums:
            for j in range(32):
                count[j] = count[j]+1 if i&1 else count[j]-1
                i=i>>1 # is this crct?
        total,n=0, len(nums)
        #print(count)
        for i in range(32):
            total+= ((n-abs(count[i]))//2) * ((n-abs(count[i]))//2 +abs(count[i]))
        
        return total