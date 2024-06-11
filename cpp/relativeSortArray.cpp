#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

// Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
//Output: [2,2,2,1,4,3,3,9,6,7,19]
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> mp;
        vector<int> r;

        for (int i = 0; i < arr1.size(); i++) {
            mp[arr1[i]] += 1;
        }

        int inserted = 0;
        for (int i = 0; i < arr2.size(); i++) {
            if (mp[arr2[i]]) {
                for (int k = 0; k < mp[arr2[i]]; k++) r.push_back(arr2[i]);
            }
        }


        

        
        



    }
};