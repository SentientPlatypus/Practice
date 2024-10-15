#include <string>
#include <vector>


using namespace std;


class Solution {
public:
    long long minimumSteps(string s) {
        int n = s.length();
        long long swaps = 0;
        long long black = 0;

        for (int i = 0; i < n; i++) {
            swaps += (s[i] == '0')? black : 0;
            black += (s[i] == '1')? 1 : 0;
        }
        return swaps;
    }
};