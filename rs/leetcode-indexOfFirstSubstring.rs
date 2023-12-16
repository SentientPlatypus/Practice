impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.len() > haystack.len() {return -1;}

        for i in 0..haystack.len() {
            for k in 0..needle.len() {
                if i + k >= haystack.len() || haystack.as_bytes()[i + k] != needle.as_bytes()[k] {break;}
                if k == needle.len() - 1 {return i as i32;}
            }
        }
        -1
    }
}