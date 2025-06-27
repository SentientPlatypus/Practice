#include <string>
#include <algorithm>
#include <math.h>
using namespace std;


class Solution {
public:
    int longestSubsequence(string s, int k) {
        reverse(s.begin(), s.end());
        int n = s.size();
        int ans = 0;


        for (int i = 0; i < n; ++i) {
            int curans = 0;
            int curnum = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '0') {
                    curans++;
                } else {
                    curnum += (1 << (j - i));
                    if (curnum <= k) {
                        curans++;
                    } else {
                        break;
                    }
                }
            }
            ans = max(ans, curans);
        }
        return ans;


    }
};