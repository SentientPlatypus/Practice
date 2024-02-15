use std::cmp::Reverse;

impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {
        let mut nums = nums;
        nums.sort_by_key(|&x| Reverse(x));

        let mut start = 0;

        while start < nums.len() {
            let mut sum:i64 = 0;
            for i in start + 1..nums.len() {
                sum += nums[i] as i64;
            }
            if sum <= nums[start] as i64 {
                start +=1;
                continue;
            }
            else {
                return sum + nums[start] as i64;
            }
        }
        -1 
    }
}