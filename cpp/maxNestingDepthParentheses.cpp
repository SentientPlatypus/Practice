#include <string>

using namespace std;

class Solution {
public:
    int maxDepth(string s) {
        int maxc = 0;
        int count = 0;
        for (char c : s) {
            if (c == '(') count++;
            else if (c == ')') count --;
            else {}
            maxc = max(count, maxc);
        }
        return maxc;
    }
};