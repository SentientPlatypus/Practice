#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int minimumDeletions(string s) {
        int totala = 0;
        
        for (char c : s) if (c == 'a') totala++;


        vector<int> adja(s.length(), s.length()); 
        vector<int> adjb(s.length(), s.length());

        int b_before = 0;
        int a_after = totala;

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (c == 'a') a_after--;
            adjb[i] = b_before;
            adja[i] = a_after;
            if (c == 'b') b_before ++;
        }


        int res = s.length();
        for (int i = 0; i < s.length(); i++) {
            // cout << adja[i] << " " << adjb[i] << "\n";
            res = min(res, adja[i] + adjb[i]);
        }
        return res;
    }
};