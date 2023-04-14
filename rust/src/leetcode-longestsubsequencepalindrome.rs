impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let n = s.len();
        let chars: Vec<char> = s.chars().collect();
        let mut f = vec![vec![0; n]; n];

        for len in 1..n + 1 {
            for i in 0..n - len + 1 {
                let j = i + len - 1;

                if i == j {
                    f[i][j] = 1;
                } else {
                    if chars[i] == chars[j] {
                        f[i][j] = f[i + 1][j - 1] + 2;
                    } else {
                        f[i][j] = f[i + 1][j].max(f[i][j - 1]);
                    }
                }
            }
        }

        f[0][n - 1]
    }
}