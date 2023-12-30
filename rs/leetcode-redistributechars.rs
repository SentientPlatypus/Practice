use std::collections::HashMap;
impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let mut m:HashMap<char, i32> = HashMap::new();
        let total = words.len() as i32;
        for word in words {
            for c in word.chars() {
                let count = m.entry(c).or_insert(0);
                *count += 1;
            }
        }


        for (_, &value) in &m {
            if value % total != 0 {
                return false;
            }
        }
        true
    }
}