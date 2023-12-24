#include <string>
using namespace std;
class Solution {
public:
    int minOperations(string s) {
        int changes01 = 0;  
        int changes10 = 0; 


        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && s[i] != '0') {
                changes01++;
            } else if (i % 2 == 1 && s[i] != '1') {
                changes01++;
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && s[i] != '1') {
                changes10++;
            } else if (i % 2 == 1 && s[i] != '0') {
                changes10++;
            }
        }

        return min(changes01, changes10);
    }
};

