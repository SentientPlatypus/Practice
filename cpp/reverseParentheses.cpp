#include <string>
#include <stack>
#include <algorithm>
#include <stack>

using namespace std;


// Input: s = "(ed(et(oc))el)"
// Output: "leetcode"
// Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> st;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') st.push(i);
            else if (s[i] == ')') {
                int lastopen = st.top();
                st.pop();

                reverse(s.begin() + lastopen, s.begin() + i);
            }
        }

        s.erase(std::remove(s.begin(), s.end(), '('), s.end());
        s.erase(std::remove(s.begin(), s.end(), ')'), s.end());

        return s;
    }
};  