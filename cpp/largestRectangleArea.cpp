#include <vector>
#include <stack>
#include <iostream>
using namespace std;

class Solution {
public:

    vector<int> getLeftLimits(vector<int>& heights) {
        stack<int> st;
        vector<int> v(heights.size(), 0);
        st.push(0);
        v.push_back(0);

        for (int i = 1; i < heights.size(); i++) {
            
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }
            if (st.empty()) {
                v[i] = 0;
                st.push(i);
            }
            else v[i] = st.top() + 1;
            st.push(i);
        }
        return v;
    }

    vector<int> getRightLimits(vector<int>& heights) {
        stack<int> st;
        vector<int> v(heights.size(), 0);

        for (int i = heights.size() - 1; i >= 0; i--) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }
            if (st.empty()) {
                v[i] = heights.size() - 1;
            } else {
                v[i] = st.top() - 1;
            }
            st.push(i);
        }
        return v;
    }


    int largestRectangleArea(vector<int>& heights) {
        int m = 0;
        vector<int> l = getLeftLimits(heights);
        vector<int> r = getRightLimits(heights);

        for (int i : v) {cout << i;}
        cout << endl;

        for (int i = 0; i < heights.size(); i ++) {
            m = max(heights[i] * (r[i] - l[i] + 1), m);
        }        
        return m;
    }
};