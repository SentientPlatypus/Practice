impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        let mut xs: Vec<i32> = points.iter().map(|c| c[0]).collect();

        xs.sort();

        let mut maxgap = -1;

        for i in 0..xs.len() - 1 {
            maxgap = maxgap.max(xs[i + 1] - xs[i]);
        }

        maxgap
    }
}