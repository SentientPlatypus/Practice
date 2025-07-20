#include <string>
using namespace std;


class Solution {
public:
    bool isValid(string word) {
        int n = word.size();
        if (word.size() < 3) return false;

        bool hasVowel = false;
        bool hasConsonant = false;
        for (int i = 0; i < n; i++) {
            char c = tolower(word[i]);
            if (c == '$' || c =='#' || c == '@') return false;

            if (c == 'a' || c == 'e' || c == 'i' || 
                c == 'o' || c == 'u') {
                hasVowel = true;
            } else if (c >= 'b' && c <= 'z') {
                hasConsonant = true;
            }
        }
        return hasVowel && hasConsonant;
    }
};

        
