#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
class Solution {
public:
    int findMaxK(vector<int>& nums) {
    
        unordered_set<int> s;
        int m = -1;

        for (int i : nums) {
            s.insert(i);
            if (s.find(-i) !=s.end()) m = max(m, abs(i));
        }
        return m;
    }
};