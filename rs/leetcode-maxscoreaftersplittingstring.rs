impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut maxs = 0;
        let mut zeros = 0;
        let mut ones = s.chars().filter(|&c| c == '1').count() as i32;

        for (i, c) in s.chars().enumerate().take(s.len() - 1) {
            zeros += if c == '0' { 1 } else { 0 };
            ones -= if c == '1' { 1 } else { 0 };
            maxs = maxs.max(zeros + ones);
        }
        maxs
    }
}