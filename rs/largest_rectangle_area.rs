impl Solution {
    fn get_left_limits(heights: &[i32]) -> Vec<i32> {
        let mut st = vec![];
        let mut v = vec![0; heights.len()];
        st.push(0);

        for i in 1..heights.len() {
            while !st.is_empty() && heights[*st.last().unwrap()] >= heights[i] {
                st.pop();
            }
            if st.is_empty() {
                v[i] = 0;
                st.push(i);
            } else {
                v[i] = *st.last().unwrap() as i32 + 1;
                st.push(i);
            }
        }
        v
    }

    fn get_right_limits(heights: &[i32]) -> Vec<i32> {
        let mut st = vec![];
        let mut v = vec![0; heights.len()];

        for i in (0..heights.len()).rev() {
            while !st.is_empty() && heights[*st.last().unwrap()] >= heights[i] {
                st.pop();
            }
            if st.is_empty() {
                v[i] = (heights.len() - 1) as i32;
            } else {
                v[i] = *st.last().unwrap() as i32 - 1;
            }
            st.push(i);
        }
        v
    }

    fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut m = 0;
        let l = Solution::get_left_limits(&heights);
        let r = Solution::get_right_limits(&heights);

        for i in 0..heights.len() {
            m = m.max(heights[i] * (r[i] - l[i] + 1));
        }
        m
    }
}

