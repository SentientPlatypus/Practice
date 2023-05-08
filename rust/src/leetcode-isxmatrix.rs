impl Solution {
    pub fn check_x_matrix(grid: Vec<Vec<i32>>) -> bool {
        let mut possible:Vec<(usize, usize)> = Vec::new();

        let mut left = (0,0);
        let mut right = (0, grid.len() - 1);
        for i in 0..grid.len() {
            possible.push(left);
            possible.push(right);

            left.0 += 1;
            left.1 += 1;
            right.0 +=1;
            right.1 -=1;
        }

        for row in 0..grid.len() {
            for col in 0..grid[0].len() {
                if !possible.contains(&(row, col)) && grid[row][col] != 0 {
                    return false
                }
            }
        }
        possible.into_iter().all(|x| grid[x.0][x.1] != 0)
    }
}