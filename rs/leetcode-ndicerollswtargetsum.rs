impl Solution {
    const M:i64 = 1_000_000_007;
    pub fn num_rolls_to_target(n: i32, k: i32, target: i32) -> i32 {
        let mut dp:Vec<Vec<i64>> = vec![vec![-1; (target + 1) as usize]; (n + 1) as usize];
        Solution::recursion(&mut dp, n, k, target) as i32
    }
    fn recursion(dp: &mut Vec<Vec<i64>>, n: i32, k: i32, target: i32) -> i64 {
        if target == 0 && n == 0 {
            return 1;
        }

        if n == 0 || target <= 0 {
            return 0;
        }

        if dp[n as usize][target as usize] != -1 {
            return dp[n as usize][target as usize] % Solution::M;
        }

        let mut ways = 0;
        for i in 1..=k {
            ways = (ways + Solution::recursion(dp, n - 1, k, target - i) % Solution::M) % Solution::M;
        }

        dp[n as usize][target as usize] = ways;
        dp[n as usize][target as usize]
    }
}