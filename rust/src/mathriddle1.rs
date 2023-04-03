fn main() {
    let mut count = 0;
    let mut numstring:String;
    for i in 0..=500 {
        numstring = i.to_string();
        for substr in numstring.chars() {
            if substr == '1' {
                count +=1;
            }
        }
    }
    println!("{}", count);
}