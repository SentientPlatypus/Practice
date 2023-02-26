use std::cmp;
impl Solution {

    pub fn verify_palindrome(bytes: &[u8]) -> bool {
        let mut left:usize = 0;
        let mut right:usize = bytes.len() - 1;
        while right > left && left >= 0 {
            if bytes[left] != bytes[right] {
                return false;
            }
            right -= 1;
            left += 1;
        }
        true
    }

    pub fn longest_palindrome(s: String) -> String {
        // println!("{}", Solution::verify_palindrome(String::from("ba").as_bytes()));

        let bytess = s.as_bytes();
        let mut left:usize = 0;
        let mut right:usize = 0;
        let mut longest:String = String::from("");
        let mut charvec = Vec::new();

        while left < s.len() {

            right = bytess.len();
            while right > left {
                right -= 1;
                if bytess[left] == bytess[right] {
                    charvec.push(right);
                }
            }

            if s.len() == 1 {
                charvec.push(0)
            }
            
            // println!("{:#?}", charvec);
            for rindex in &charvec {
                let mut substr = &bytess[left..rindex + 1];
                let sub_string = String::from(&s[left..rindex + 1]);
                // println!("str:{}, l:{}, r:{}", sub_string, left, rindex);
                if Solution::verify_palindrome(substr) {
                    longest = if longest.len() >= sub_string.len() {longest} else {sub_string};
                    break;
                }
            }
            left += 1;
            charvec = Vec::new();
        }
        longest
    }
}