#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int i, j, key;

        for (i = 1; i < nums.size(); i++) {
            key = nums[i];
            j =  i - 1;

            while (j >= 0 && nums[j] > key) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }
        return nums;
    }
};