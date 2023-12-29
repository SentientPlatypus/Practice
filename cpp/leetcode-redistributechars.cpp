#include <string>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool makeEqual(vector<string>& words) {
        unordered_map<char, int> map;

        for (int i = 0; i < words.size(); i ++ ) {

            for (char c: words[i]) {
                map[c] += 1;
            }
        }

        int total = words.size();
        for (const auto& pair : map) {
            if (pair.second % total != 0) {
                return false;
            }
        }
        return true;
    }
};