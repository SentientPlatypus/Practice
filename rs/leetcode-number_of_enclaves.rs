use std::collections::{HashSet, VecDeque};

impl Solution {

    fn neighbors(r: usize, c: usize, grid: &Vec<Vec<i32>>) -> Vec<(usize, usize)> {
        vec![
            (r + 1, c),
            (r - 1, c),
            (r, c + 1),
            (r, c - 1),
        ]
        .into_iter()
        .filter(|&(x, y)| {
            x < grid.len()
                && y < grid[0].len()
                && grid[x][y] == 1
        })
        .collect()
    }

    fn get_land_on_outer_edge(grid: &Vec<Vec<i32>>) -> Vec<(usize, usize)> {
        let mut land_spots_on_edge:Vec<(usize, usize)> = Vec::new();

        for c in 0..grid[0].len() {
            land_spots_on_edge.push((0, c));
            land_spots_on_edge.push((grid.len() - 1, c))
        }

        for r in 0..grid.len() {
            land_spots_on_edge.push((r, 0));
            land_spots_on_edge.push((r, grid[0].len() - 1))
        }
        land_spots_on_edge.into_iter().filter(|&(r, c)| grid[r][c] == 1).collect()
    }

    fn get_total_lands(grid:&Vec<Vec<i32>>) ->i32 {
        let mut count:i32 = 0;
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] == 1 {
                    count += 1;
                }
            }
        }
        count
    }

    pub fn num_enclaves(grid: Vec<Vec<i32>>) -> i32 {
        let mut count:i32 = 0;
        let spots:Vec<(usize, usize)> = Solution::get_land_on_outer_edge(&grid);
        // println!("{:#?}", spots);
        let mut q:VecDeque<(usize, usize)> = VecDeque::new();
        let mut visited:HashSet<(usize, usize)> = HashSet::new();

        for p in spots {
            if !visited.contains(&p) {
                q.push_back(p);
                while q.len() > 0 {
                    let current = q.pop_front().expect("failed to pop");

                    visited.insert(current);
                    count += 1;

                    println!("{} {}", current.0, current.1);
                    for n in Solution::neighbors(current.0, current.1, &grid) {
                        if !visited.contains(&n) {
                            q.push_back(n);
                            visited.insert(n);
                        }
                    }

                }
            }    
        }
        Solution::get_total_lands(&grid)-count
    }
}