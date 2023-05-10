enum Direction {
    Up,
    Down,
    Left,
    Right
}
use std::collections::HashSet;
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut p:(usize, usize) = (0,0);
        let mut d:Direction = Direction::Right;
        let mut visited:HashSet<(usize, usize)> = HashSet::new();
        let mut l:Vec<i32> = Vec::new();

        while visited.len() < matrix.len() * matrix[0].len() {
            visited.insert(p);
            l.push(matrix[p.0][p.1]);

            match d {
                Direction::Up=> {
                    if p.0 == 0 || visited.contains(&(p.0 - 1, p.1)) {
                        d = Direction::Right;
                    }
                },
                Direction::Down => {
                    if p.0 == matrix.len() - 1 || visited.contains(&(p.0 + 1, p.1)) {
                        d = Direction::Left;
                    }
                },    
                Direction::Left => {
                    if p.1 == 0 || visited.contains(&(p.0, p.1 - 1)) {
                        d = Direction::Up;
                    }
                },    
                Direction::Right => {
                    if p.1 == matrix[0].len()-1 || visited.contains(&(p.0, p.1 + 1)) {
                        d = Direction::Down;
                    }
                },                
            };

            match d {
                Direction::Up => {
                    p.0 -=1;
                },
                Direction::Down => {
                    p.0 +=1;
                },
                Direction::Left => {
                    p.1 -= 1;
                },
                Direction::Right => {
                    p.1 +=1;
                }
            };
        }
        l
    }
}