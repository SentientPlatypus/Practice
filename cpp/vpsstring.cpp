#include <string>

using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
        int leftCount = 0, rightCount = 0;
        
        for (char c : s) {
            leftCount += c == '(' ? 1 : -1;
            rightCount += c == ')' ? -1 : 1;
            
            if (rightCount < 0) {
                break;
            }
            
            leftCount = max(leftCount, 0);
        }

        return leftCount == 0;
    }
};