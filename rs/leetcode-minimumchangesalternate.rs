impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut changes_01 = 0;
        let mut changes_10 = 0;

        for (i, c) in s.chars().enumerate() {
            if i % 2 == 0 && c != '0' {
                changes_01 += 1;
            } else if i % 2 == 1 && c != '1' {
                changes_01 += 1;
            }
        }

        for (i, c) in s.chars().enumerate() {
            if i % 2 == 0 && c != '1' {
                changes_10 += 1;
            } else if i % 2 == 1 && c != '0' {
                changes_10 += 1;
            }
        }

        changes_01.min(changes_10)
    }
}