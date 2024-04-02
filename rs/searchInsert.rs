impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1;
        let mut m:usize = 0;

        if target < nums[0] {return 0;}

        while l <= r {
            m = (l + r) / 2;

            if nums[m] == target {return m as i32;}
            else if nums[m] < target {l = m + 1;}
            else {r = m - 1;}
        }

        if l < nums.len() && nums[l] < target {return (l + 1) as i32;}
        l as i32
    }
}