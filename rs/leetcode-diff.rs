impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut diff = vec![vec![0; grid[0].len()]; grid.len()];
        let mut ones_row = vec![0; grid.len()];
        let mut ones_col = vec![0; grid[0].len()];
        let mut zeros_row = vec![0; grid.len()];
        let mut zeros_col = vec![0; grid[0].len()];

        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] == 1 {
                    ones_row[r] += 1;
                    ones_col[c] += 1;
                }
                if grid[r][c] == 0 {
                    zeros_row[r] += 1;
                    zeros_col[c] += 1;
                }
            }
        }

        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                diff[r][c] = ones_row[r] + ones_col[c] - zeros_row[r] - zeros_col[c];
            }
        }

        diff
    }
}