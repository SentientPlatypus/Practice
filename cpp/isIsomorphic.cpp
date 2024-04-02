#include <unordered_map>
#include <string>

using namespace std;
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> ts;
        unordered_map<char, char> st;

        for (int i = 0; i < s.length(); i ++) {
            if (st.find(s[i]) == st.end()) {
                st[s[i]] = t[i];

                if (ts.find(t[i]) == ts.end()) ts[t[i]] = s[i];

                else if (ts[t[i]] != s[i]) return false;

            }
            else if (st[s[i]] != t[i]) return false;
        }
        return true;
    }
};