#include <string>
#include <algorithm>
#include <math.h>
using namespace std;


class Solution {
public:
    int longestSubsequence(string s, int k) {
        int sm = 0;
        int cnt = 0;
        int bits = 32 - __builtin_clz(k);
        
        for (int i = s.size() - 1; i >= 0; i--) {
            char ch = s[i];
            int pos = s.size() - 1 - i;
            if (ch == '1') {
                if (pos < bits && sm + (1 << pos) <= k) {
                    sm += 1 << pos;
                    cnt++;
                }
            } else {
                cnt++;
            }
        }
        return cnt;
    }
};