impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut maxi = 0;
        let mut smaxi = if nums[0] > nums[1] { 1 } else { 0 };

        let mut lowi = 0;
        let mut slowi = if nums[0] < nums[1] { 1 } else { 0 };

        for i in 0..nums.len() {
            if nums[i] > nums[maxi] {
                smaxi = maxi;
                maxi = i;
            }
            else if nums[i] > nums[smaxi] && i != maxi {
                smaxi = i;
            }
            if nums[i] < nums[lowi] {
                slowi = lowi;
                lowi = i;
            }
            else if nums[i] < nums[slowi] && i != lowi {
                slowi = i;
            }
        }

        (nums[maxi] * nums[smaxi]) - (nums[lowi] * nums[slowi])
    }
}