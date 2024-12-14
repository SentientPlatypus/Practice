#include <vector>
#include <string>
#include <iostream>

using namespace std;




class Solution {
public:
    bool isMatch(string s, string p) {
        if (s.size() == 0) { //works

            if (p.size() == 0) {
                return true;
            }
            else if (p[0] != '*') {
                return false;
            }
        }
        

        char snext = s[0];
        char pattern = p[0];
        

        if (pattern == '*') {
            
            int i = 0;
            while (p[i] == '*') { //go until i doesnt point to *
                i++;
            }

            if (i == p.length()) return true;

            bool works = false;

            for (int k = 0; k <= s.size(); k++) {
                works |= isMatch(s.substr(k), p.substr(i));
            }

            return works;

        }
        else if (pattern == '?') {
            return isMatch(s.substr(1), p.substr(1));
        }
        else {
            return snext == pattern && isMatch(s.substr(1), p.substr(1));
        }
    }
};