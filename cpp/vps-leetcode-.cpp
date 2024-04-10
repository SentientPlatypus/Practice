#include <map>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        map<char, char> mp = {{'(',')'},{'[',']'},{'{','}'}};

        stack<int> st; 

        for (int i = 0; i < s.length(); i ++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') st.push(s[i]);
            else {
                if (!st.empty()) {
                    if ((st.top() == '(' || st.top() == '[' || st.top() == '{') && mp[st.top()]  == s[i]) st.pop();
                    else return false;
                }
                else return false;
            }
        }

        return (!st.empty())? false: true;
    }
};