use std::cmp;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut first:usize = 0;
        let mut last:usize = height.len() - 1;
        let mut max_area:i32 = 0;
        while first < last {
            let area = (last - first) as i32 * cmp::min(&height[first], &height[last]);
            max_area = cmp::max(area, max_area);
            if &height[first] < &height[last] {
                first += 1;
            }
            else {
                last -= 1;
            }
        }
        max_area
    }
}