use std::collections::HashMap;
use std::cmp;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut storage = HashMap::new();

        let mut c = 0;
        let mut finalC = 0;
        let mut i:usize = 0;

        while i < s.len() {
            let current = s.as_bytes()[i];
            match storage.get(&current) {
                Some(n) => {
                    finalC = cmp::max(finalC, c);
                    i = n + 1;
                    c = 0;
                    storage = HashMap::new();
                },
                None => {
                    storage.insert(current, i);
                    c += 1;
                    i += 1;
                }
            }
        }

        cmp::max(finalC, c)

    }
}