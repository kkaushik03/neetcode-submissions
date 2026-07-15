class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 3) return 0;

        int left = 0, right = height.size() - 1;
        int leftMax = 0, rightMax = 0;
        int result = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                // left side is the bottleneck
                if (height[left] >= leftMax)
                    leftMax = height[left];      // new wall, no water here
                else
                    result += leftMax - height[left];
                left++;
            } else {
                // right side is the bottleneck
                if (height[right] >= rightMax)
                    rightMax = height[right];
                else
                    result += rightMax - height[right];
                right--;
            }
        }
        return result;
    }
};