impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let n = s.len();
        let mut dp = vec![0; n + 1];
        dp[n] = 1;

        for i in (0..n).rev() {
            if s.chars().nth(i).unwrap() != '0' {
                dp[i] += dp[i + 1];
            }
            if i + 1 < n && (s.chars().nth(i).unwrap() == '1' || (s.chars().nth(i).unwrap() == '2' && s.chars().nth(i + 1).unwrap() <= '6')) {
                dp[i] += dp[i + 2];
            }
        }

        dp[0]
    }
}
