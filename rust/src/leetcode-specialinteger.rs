impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let mut maxcount:i32 = 0;
        let mut maxnum:i32 = arr[0];

        let mut current:i32 = arr[0];
        let mut timesappeared:i32 = 0;

        for i in 0..arr.len() {
            if arr[i] == current {
                timesappeared +=1;
            }
            else {
                if timesappeared > maxcount {
                    maxcount = timesappeared;
                    maxnum = current;
                }
                timesappeared = 1;
                current = arr[i];
            }
        }

        if timesappeared > maxcount {
            maxnum = current;
        }
        maxnum
    }
}