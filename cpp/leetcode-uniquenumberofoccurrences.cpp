#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> m;

        for (int &k : arr) {
            m[k] += 1;
        }

        unordered_map<int, int> o;
        for (const auto& n : m) {
            o[n.second] += 1;
        }

        for (const auto& n : o) {
            if (n.second != 1) return false;
        }

        return true;

    }
};