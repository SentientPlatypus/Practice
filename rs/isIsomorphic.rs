use std::collections::HashMap;
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut ts:HashMap<u8, u8> = HashMap::new();
        let mut st:HashMap<u8, u8> = HashMap::new();

        for (i, &ch) in s.as_bytes().iter().enumerate() {
            match st.get(&ch) {
                None => {
                    st.insert(ch, t.as_bytes()[i]);
                    match ts.get(&t.as_bytes()[i]) {
                        None => {
                            ts.insert(t.as_bytes()[i], ch);
                        }
                        Some(&val) => {
                            if val != ch {
                                return false;
                            }
                        }
                    }
                }
                Some(&val) => {
                    if val != t.as_bytes()[i] {
                        return false;
                    }
                }
            }
        }
        true
    }
}