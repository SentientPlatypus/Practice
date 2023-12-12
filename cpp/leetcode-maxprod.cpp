#include <vector>
#include <iostream>

class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        int h = 0;
        int secondh = 0;

        for (int i : nums) {
            if (i > h) {
                secondh = h;
                h = i;
            } 
            else if (i > secondh) {
                secondh = i;
            }
        }

        return (h-1)*(secondh-1);
    }
};


int main() {
    Solution s;

    std::vector<int> nums;
    
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }

    std::cout << s.maxProduct(nums) << std::endl;


    return 0;
}