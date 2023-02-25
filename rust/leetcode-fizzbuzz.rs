impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        if n == 1 {
            let mut myVec:Vec<String> = Vec::new();
            myVec.push(String::from("1"));
            return myVec;
        }
        let mut prevVec:Vec<String> = Solution::fizz_buzz(n - 1);
        if n % 3 == 0 && n % 5 == 0 {
            prevVec.push(String::from("FizzBuzz"));
        }
        else if n % 3 == 0{
            prevVec.push(String::from("Fizz"));
        }
        else if n % 5 == 0 {
            prevVec.push(String::from("Buzz"));
        }
        else {
            prevVec.push(format!("{}", n))
        }
        prevVec
    }
}