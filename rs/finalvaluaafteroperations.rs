impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut n = 0;
        for s in operations {
            if s.contains('+') {n+=1;}
            else {n-=1;}
        }
        n
    }
}