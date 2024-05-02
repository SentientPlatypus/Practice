use std::collections::HashSet;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut s:HashSet<i32> = HashSet::new();
        let mut m:i32 = -1;

        for i in 0..nums.len() {
            s.insert(nums[i]);
            if s.contains(&-nums[i]) {
                m = m.max(nums[i].abs());
            }
        }
        return m;
    }
}