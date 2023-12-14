impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        match dividend.checked_div(divisor) {
            Some(n) => return n,
            None => {
                if (dividend < 0 && divisor < 0) || (dividend > 0 && divisor > 0){
                    return i32::MAX
                }
                return i32::MIN
            }
        }
    }
}
