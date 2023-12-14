
use std::io;

fn max_product(nums: &Vec<i32>) -> i32 {
    let mut h = 0;
    let mut second_h = 0;

    for &i in nums {
        if i > h {
            second_h = h;
            h = i;
        } else if i > second_h {
            second_h = i;
        }
    }

    return (h-1)*(second_h-1);
}

fn main() {
    let mut nums = Vec::new();

    let mut n = String::new();
    io::stdin().read_line(&mut n)
        .expect("Failed to read input");

    let n: usize = n.trim().parse()
        .expect("Failed to parse input");

    for _ in 0..n {
        let mut num = String::new();
        io::stdin().read_line(&mut num)
            .expect("Failed to read input");
        let num: i32 = num.trim().parse()
            .expect("Failed to parse input");
        nums.push(num);
    }

    let result = max_product(&nums);
    println!("{}", result);
}
