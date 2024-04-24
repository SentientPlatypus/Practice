#include <vector>
using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 2 || n == 1) return 1;
        if (n == 3) return 2;

        vector<int> terms(n + 1, 0);
        terms[0] = 0;
        terms[1] = 1;
        terms[2] = 1;
        for (int t = 3; t <=n; t++) {
            terms[t] = terms[t - 1] + terms[t - 2] + terms[t-3];
        }
        return terms[n];
    }
};