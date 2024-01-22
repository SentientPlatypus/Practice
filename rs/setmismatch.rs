impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut r:Vec<i32> = vec![0;2];
        let mut n:Vec<i32> = vec![0; nums.len() + 1];

        for i in nums {
            n[i as usize] += 1;
        }

        for i in 1..n.len() {
            if n[i] == 2 {
                r[0] = i as i32;
            }
            if n[i] == 0 {
                r[1] = i as i32;
            }
        }
        r
    }
}