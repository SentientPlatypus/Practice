impl Solution {
    pub fn get_jump(num_rows: i32) -> i32 {
        if num_rows == 1 {
            return 1;
        }
        return (num_rows - 1) * 2;
    }



    pub fn convert(s: String, num_rows: i32) -> String {
        let bytes = s.as_bytes();
        let mut r:String = String::from("");
        let jump = Solution::get_jump(num_rows);
        let mut rowcounter = 0;
        let mut index:usize = 0;

        while rowcounter < num_rows {
            index = rowcounter as usize;
            let evenjump = jump - Solution::get_jump(rowcounter + 1);
            let oddjump = jump - evenjump;
            let mut isEven:bool = true;
            
            while index < s.len() {
                let current = bytes[index] as char;
                r.push(current);
                if rowcounter == 0 || rowcounter == num_rows - 1{
                    index += jump as usize;
                }
                else {
                    index += if isEven {evenjump as usize} else {oddjump as usize};
                    isEven = isEven == false;
                }
            }
            rowcounter += 1;
        }
        r
    }
}