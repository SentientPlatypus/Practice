impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut dp:Vec<i32> = vec![0; (n + 1) as usize];
        Solution::fib(n, &mut dp)
    }

    fn fib(n:i32, dp:&mut Vec<i32>) -> i32{
        if n <=3 {return n;}
        if dp[n as usize] != 0 {return dp[n as usize];}
        dp[n as usize] = Solution::fib(n - 1, dp) + Solution::fib(n - 2, dp);
        dp[n as usize]
    }
}