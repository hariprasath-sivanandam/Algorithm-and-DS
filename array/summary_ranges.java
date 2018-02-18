https://leetcode.com/problems/summary-ranges

Question:

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]


Solution:
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int i=0, start;
        while(i<nums.length){
            sb.delete(0, sb.length());
            start =i;
            sb.append(String.valueOf(nums[i]));
            while(i<nums.length-1 && nums[i]+1 == nums[i+1])i++;
            if(i<nums.length && i!=start)
                sb.append("->").append(String.valueOf(nums[i]));
            i++;
            res.add(sb.toString());
        }
        return res;
    }
}

// notes:
// inner loop boundary check & if check for i value
// string builder clear