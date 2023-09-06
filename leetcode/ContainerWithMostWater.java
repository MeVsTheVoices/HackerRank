class Solution {
    public int maxArea(int[] height) {
        int top = height.length - 1;
        int bottom = 0;
        int maxArea = Integer.MIN_VALUE;
        while(top > bottom) {
            int width = top - bottom;
            int maxHeight = Math.min(height[top], height[bottom]);
            int area = width * maxHeight;
            if (area > maxArea)
                maxArea = area;
            if (height[bottom] < height[top]) 
                bottom++;
            else
                top--;
        }
        return maxArea;
    }
}