use std::collections::VecDeque;
impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        fn neighbors(su:usize, sc:usize, img:&Vec<Vec<i32>>) -> Vec<(usize, usize)> {
            let mut results:Vec<(usize, usize)> = Vec::new();

            let poss_neighbors:Vec<(usize, usize)> = vec![
                (su + 1, sc),
                (su - 1, sc),
                (su, sc + 1),
                (su, sc - 1)
            ];

            for t in &poss_neighbors {
                if t.0 >= 0 && t.0 < img.len() && t.1 >=0 && t.1 < img[0].len() {
                    results.push(*t);
                }
            }
            results
        }


        let mut q = VecDeque::new();
        let mut visited:Vec<(usize, usize)> = Vec::new();

        q.push_back((sr as usize, sc as usize));

        let mut currect:(usize, usize);

        while q.len() > 0 {
            let current = q.pop_front().expect("failed to pop");

            let prev_val = image[current.0][current.1];
            image[current.0][current.1] = color;

            for neighbor in neighbors(current.0, current.1, &image) {
                if !(visited.contains(&neighbor)) && image[neighbor.0][neighbor.1] == prev_val {
                    visited.push(neighbor);
                    q.push_back(neighbor);
                }
            }
        }
        image
    }
}