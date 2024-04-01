impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut words: Vec<&str> = s.split_whitespace().collect();
        if let Some(last_word) = words.pop() {
            return last_word.len() as i32;
        }
        0
    }
}