#include <string>
using namespace std;


class Solution {
public:
    bool isValid(string word) {
        int n = word.size();
        for (int i = 0; i < n; i++) {
            if (!isalpha(word[i])) return false;
        }
        return true;
    }
};

        
    }
};