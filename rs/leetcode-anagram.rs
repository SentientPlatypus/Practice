use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut char_count: HashMap<char, i32> = HashMap::new();

        for ch in s.chars() {
            *char_count.entry(ch).or_insert(0) += 1;
        }

        for ch in t.chars() {
            if let Some(count) = char_count.get_mut(&ch) {
                *count -= 1;
                if *count < 0 {
                    return false;
                }
            } else {
                return false;
            }
        }

        char_count.values().all(|&count| count == 0)
    }
}