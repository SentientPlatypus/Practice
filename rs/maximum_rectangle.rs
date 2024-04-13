impl Solution {
    fn get_histograms(matrix: &Vec<Vec<char>>) -> Vec<Vec<i32>> {
        let mut hists: Vec<Vec<i32>> = Vec::new();
        hists.push(matrix[0].iter().map(|&x| if x == '1' { 1 } else { 0 }).collect());
        for r in 1..matrix.len() {
            let mut v: Vec<i32> = vec![0; matrix[0].len()];

            for c in 0..matrix[0].len() {
                if matrix[r][c] == '1' {
                    v[c] = 1 + hists[r - 1][c];
                }
            }
            hists.push(v);
        }
        hists
    }

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

    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }
        
        let hists: Vec<Vec<i32>> = Solution::get_histograms(&matrix);
        let mut m: i32 = 0;

        for i in 0..hists.len() {
            m = m.max(Solution::largest_rectangle_area(hists[i].clone()));
        }
        m
    }
}
