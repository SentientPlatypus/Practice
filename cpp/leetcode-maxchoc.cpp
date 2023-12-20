#include <vector>

using namespace std;


class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int l = 1000;
        int sl = 999;

        for (int p:prices) {
            if (p < l) {
                sl = l;
                l = p;
            }
            else if (p < sl) {
                sl = p;
            }
        }

        return (money - l - sl < 0)? money : money - l - sl;
        
    }
};