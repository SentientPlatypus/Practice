#include <unordered_map>
#include <string>
class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::unordered_map<char, int> charCount;

        for (char ch : s) {
            charCount[ch]++;
        }

        for (char ch : t) {
            charCount[ch]--;
            if (charCount[ch] < 0) {
                return false;
            }
        }

        for (const auto& entry : charCount) {
            if (entry.second != 0) {
                return false;
            }
        }

        return true;
    }
};
