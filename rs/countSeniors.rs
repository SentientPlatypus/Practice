impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        let mut count = 0;
        for s in details {
            if s[11..13].parse::<i32>().unwrap_or(0) > 60 {
                count += 1;
            }
        }
        count
    }
}