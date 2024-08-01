#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countSeniors(vector<string>& details) {
        int count = 0;
        for (string s : details) count += stoi(s.substr(11, 2)) > 60;
        return count;
    }
};