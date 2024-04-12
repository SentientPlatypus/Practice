#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& h) {
        int l = 0;
        int r = h.size() - 1;
        int lmax = -1;
        int rmax = -1;
        int total = 0;

        while(l<r){
            lmax=max(lmax,h[l]);
            rmax=max(rmax,h[r]);
            total += (lmax<rmax)? lmax-h[l++] : rmax-h[r--];
        }
        return total;
    }
};


