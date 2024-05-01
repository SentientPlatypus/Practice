#include <string>

using namespace std;
class Solution {
public:
    string reversePrefix(string word, char ch) {
        int l = word.find(ch);
        if (l == -1) return word;

        for (int i = 0; i <= l / 2 ; i ++) {
            swap(word[i], word[l - i]);
        }
        return word;
    }
};