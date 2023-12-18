#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int maxi = 0;
        int smaxi = (nums[0] > nums[1]) ? 1 : 0; 

        int lowi = 0;
        int slowi = (nums[0] < nums[1]) ? 1 : 0; 

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > nums[maxi]) {
                smaxi = maxi;
                maxi = i;
            }
            else if (nums[i] > nums[smaxi] && i != maxi) {
                smaxi = i;
            }
            if (nums[i] < nums[lowi]) {
                slowi = lowi;
                lowi = i;
            }
            else if (nums[i] < nums[slowi] && i != lowi) {
                slowi = i;
            }
        }
        cout << "maxi: " << maxi << "smaxi: " << smaxi << "\n";
        cout << "lowi: " << lowi << "slowi: " << slowi << "\n";
        return (nums[maxi] * nums[smaxi]) - (nums[lowi] * nums[slowi]);
    }
};