#include <string>
#include <vector>
using namespace std;


class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        if (s.size() % k != 0) {
            s.append(k - s.size() % k, fill);
        }

        vector<string> res;
        for (int i = 0; i < s.size(); i+=k) {
            res.push_back(s.substr(i, k));
        }
        return res;
    }
};