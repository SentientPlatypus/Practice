#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> s;
        int maxArea = 0;
        
        for (int i = 0; i <= n; ++i) {
            while (!s.empty() && (i == n || heights[s.top()] >= heights[i])) {
                int h = (i == n) ? 0 : heights[i];
                int index = s.top();
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                maxArea = max(maxArea, heights[index] * width);
            }
            s.push(i);
        }
        
        return maxArea;
    }
};
