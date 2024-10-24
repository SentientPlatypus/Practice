
#include <vector>

using namespace std;


class Solution {
public:
    void sortColors(vector<int>& nums) {
        int r = 0;
        int b = nums.size() - 1;
        int i = 0;

        while (i <= b) {
            switch (nums[i])
            {
            case 0:
                swap(nums, i++, r++);
                break;
            case 1:
                i++;
                break;
            case 2:
                swap(nums, i, b--);
                break;
            default:
                break;
            }
        }
    }

private:
    void swap(vector<int>& nums, int i, int k) {
        int temp = nums[i];
        nums[i] = nums[k];
        nums[k] = temp;
    }
};