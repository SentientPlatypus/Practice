
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minimumDeletions(string word, int k) {
        vector<int> fs(26);
        for (char c : word) {
            fs[c - 'a']++;
        }
        int ans = word.size();

        vector<int> nonzerof;
        int maxf = 0;
        for (int f : fs) {
            if (f > 0) {
                nonzerof.push_back(f);
                maxf = max(maxf, f);
            }
        }

        for (int possible_f = 1; possible_f <= maxf; possible_f++) {
            int deletions = 0;
            for (int f : nonzerof) {
                if (f > possible_f + k) {
                    deletions += f - possible_f - k;
                } else if (f < possible_f) {
                    deletions += f;
                }
            }

            ans = min(ans, deletions);
            
        }
        return ans;


        
    }
};