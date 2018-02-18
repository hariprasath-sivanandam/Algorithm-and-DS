https://leetcode.com/problems/container-with-most-water/description/

Question:
Container With Most Water.
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Solution:

class Solution {
    public int maxArea(int[] height) {
        int max_area=0;
        for(int i=0,j=height.length-1;i<j;)
        {
            max_area = Math.max(max_area, (j-i) * Math.min(height[i],height[j]));
            if(height[i]<height[j])
                i++;
            else 
                j--;
        }
        return max_area;
    }
}

//two pointer problem