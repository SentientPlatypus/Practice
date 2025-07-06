#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> counts;
        for (int num : arr) {
            counts[num]++;
        }

        int maxlucky = -1;
        for (const auto& [key, value] : counts) {
            if (key == value) {
                maxlucky = max(maxlucky, key);
            }
        }
        return maxlucky;
    }
};