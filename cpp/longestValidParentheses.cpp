#include <unordered_map>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
        int m = 0;

        stack<int> st;

        for (int i = 0; i < n; i ++) {
            if (s[i] == '(') {
                st.push(i);
            }
            else {
                if (!st.empty()) {
                    if (s[st.top()] == '(') st.pop();
                    else st.push(i);
                }
                else {
                    st.push(i);
                }
            }
        }

        if (st.empty()) return n;
        int a = n; int b = 0;
        while (!st.empty()) {
            b = st.top(); st.pop();
            m = max(m, a-b-1);
            a = b;
        }
        m = max(m, a);
        return m;
    }
};