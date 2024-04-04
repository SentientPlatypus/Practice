impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut m:i32 = 0;
        let mut count:i32 = 0;

        for c in s.chars() {
            if c == '(' {
                count +=1;
                m = m.max(count);
            }
            else if c == ')' {
                count -= 1;
            }
            else {

            }
        }
        m
    }
}