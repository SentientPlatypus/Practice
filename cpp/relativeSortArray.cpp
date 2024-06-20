#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> mp;
        vector<int> r;

        for (int i = 0; i < arr1.size(); i++) {
            mp[arr1[i]] += 1;
        }

        for (int i = 0; i < arr2.size(); i++) {
            if (mp.find(arr2[i]) != mp.end()) {
                for (int k = 0; k < mp[arr2[i]]; k++) {
                    r.push_back(arr2[i]);
                }
                mp.erase(arr2[i]);
            }
        }

        vector<int> remaining;
        for (auto it = mp.begin(); it != mp.end(); ++it) {
            for (int k = 0; k < it->second; k++) {
                remaining.push_back(it->first);
            }
        }

        sort(remaining.begin(), remaining.end());
        r.insert(r.end(), remaining.begin(), remaining.end());

        return r;
    }
};
