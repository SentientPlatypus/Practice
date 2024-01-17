use std::collections::HashMap;
impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut m:HashMap<i32, i32> = HashMap::new();
        let mut n:HashMap<i32, i32> =  HashMap::new();

        for n in arr {
            let count = m.entry(n).or_insert(0);
            *count += 1;
        }

        for (_, k) in &m {
            let count = n.entry(*k).or_insert(0);
            *count += 1;
        }

        for (_, k) in n {
            if k != 1 {
                return false;
            }
        }
        true

    }
}