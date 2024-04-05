#include <stack>
#include <cctype>
#include <string>
using namespace std;
class Solution {
public:
    string makeGood(string s) {
        if (s.length() < 2) {return s;}
        stack<char> st;
        st.push(s[0]);

        for (int i = 1; i < s.length(); i ++) {
            if (!st.empty() && tolower(s[i]) == tolower(st.top()) && st.top() != s[i]) {
                st.pop();
            }
            else {
                st.push(s[i]);
            }
        }    
        
        string r;
        while (!st.empty()) {
            r = st.top() + r;
            st.pop();
        }
        return r;
    }
};