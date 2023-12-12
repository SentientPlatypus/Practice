impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut h:i32 = 0;
        let mut secondh:i32 = 0;
        let mut current:i32;

        for i in 0..nums.len() {
            current = nums[i];
            if current > h {
                secondh = h;
                h = current;
            }
            else if current > secondh {
                secondh = current;
            }
        }

        (h-1) * (secondh - 1)
    }
}