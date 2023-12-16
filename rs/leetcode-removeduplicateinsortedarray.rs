impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i:usize = 1;

        while i < nums.len() {
            if nums[i] == nums[i - 1] {
                nums.remove(i);
                i -= 1;
            }
            i+=1;
        }
        nums.len() as i32
    }
}