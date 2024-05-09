#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end());
        int n = happiness.size();
        int originalk = k;
        long long total = 0; 
        while (k > 0 && n - (originalk - k) - 1 >= 0) { 
            total += max(0, happiness[n - (originalk - k) - 1] - (originalk - k));
            k --;
        }
        return total;
    }
};
