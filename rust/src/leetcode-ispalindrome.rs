use std::collections::VecDeque;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s:String = x.to_string();
        let bytes = s.as_bytes();

        let mut left:usize = 0;
        println!("{:#?}", bytes);

        if bytes.len() == 1 {
            return true;
        }

        while left <= bytes.len() - 1 - left {
            if bytes[left] != bytes[bytes.len() - 1 - left] {
                return false;
            }
            left += 1;
        }
        true 
    }
}