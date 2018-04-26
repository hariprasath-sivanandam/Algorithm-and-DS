#Question:

#https://leetcode.com/problems/missing-ranges/description/

#163. Missing Ranges
#Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

#Example:

#Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
#Output: ["2", "4->49", "51->74", "76->99"]

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        #testcases - [0], [2], [1,3]
        #lower start correctlty, upper starts correctly
        #upper ends correctly, 
        lower,upper = lower-1, upper+1
        nums = [lower]+nums+[upper]
        arr=[]
        for i in range(1, len(nums)):
            if(nums[i]-nums[i-1] <2):
                continue
            s = str(nums[i-1]+1)
            s+= "->"+str(nums[i]-1) if(nums[i]-nums[i-1] >2) else ""
            arr.append(s)
        return arr
    
    # note
    # modify array by adding lower and upper bound
    # introduce unifoemity in commparing
    # set range check properly in loop