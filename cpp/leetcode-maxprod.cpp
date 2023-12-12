class Solution {
public:
    int maxProduct(vector<int>& nums) {
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