impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {

        let mut strs_real:Vec<String> = Vec::new();

        for s in strs {
            strs_real.push(s);
        }


        strs_real.sort_by(|a, b| a.len().cmp(&b.len()));
        println!("{:#?}", strs_real);

        let mut index = 0;
        while index < strs_real[0].len() {
            for s in 0..strs_real.len() {
                let bytez = strs_real[s].as_bytes();
                if bytez[index] != strs_real[0].as_bytes()[index] {
                    return String::from(&strs_real[0][0..index])
                }
            }
            index += 1;


        }
        return String::from(&strs_real[0][0..index])
    }
}