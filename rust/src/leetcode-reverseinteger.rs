impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut num:String = if x > 0 {String::from("")} else {String::from("-")};
        let mut copy = if x > 0 {x} else {-x};

        if x == 0 {
            return 0;
        }

        while copy > 0 {
            num.push_str((copy % 10).to_string().as_str());
            copy /= 10;
        }
        match num.parse::<i32>() {
            Ok(n) => {n},
            Err(_) => 0
        }
    }
}