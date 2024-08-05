#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;


class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> mp;
        int tally = 0;

        for (string s : arr) {
            mp[s] ++;

        }


        for (string s : arr) {
            if (mp[s] == 1) tally += 1;
            if (tally == k) return s;
        }
        return "";

    }
};