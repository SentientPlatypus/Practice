#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int i = 0;
        for (string s : operations) {
            if (s == "X++" || s == "++X") i++;
            else i--;
        }
        return i;
    }
};