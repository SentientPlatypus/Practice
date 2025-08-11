#include <unordered_set>

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        unordered_set<int> used;

        for (int f : fruits) {
            for (int i = 0; i < baskets.size(); i++) {
                int b = baskets[i];
                if (b >= f && used.find(i) == used.end()) {
                    used.insert(i);
                    break;
                }
            }
        }

        return baskets.size() - used.size();
    }
};
