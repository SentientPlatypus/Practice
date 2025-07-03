#include <string>
using namespace std;


class Solution {
public:
    char kthCharacter(int k) {
        string s = "a";
        while (s.length() < k) {
            s += nextString(s);
        }
        return s[k - 1];
    }

    string nextString(string s) {
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'z') {
                s[i] = 'a';
            } else {
                s[i]++;
            }
        }
        return s;
    }
};

