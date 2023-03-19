


impl Solution {
    pub fn solve(self) -> u8 {
        return 0
    }
}




pub struct Solution {
    n:u8,
    s:String
}

use std::io;
fn main() {
    let mut strr:String = Default::default();
    io::stdin()
    .read_line(&mut strr)
    .expect("Failed to read line");

    let solution:Solution = Solution{
        s:strr.clone(),
        n:9
    };

    println!("{} {}", solution.n, solution.s)
}