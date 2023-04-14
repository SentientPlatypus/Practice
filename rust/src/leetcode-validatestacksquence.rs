
impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut pushedi:usize = 0;
        let mut poppedi:usize = 0;


        let mut stack:Vec<i32> = Vec::new();

        println!("POPPEDLEN:{}", popped.len());

        stack.push(pushed[pushedi]);

        while pushedi <= pushed.len() && stack.len() > 0 && poppedi < popped.len() {
            while stack.len() > 0 && poppedi < popped.len() && stack[stack.len() - 1] == popped[poppedi]{
                poppedi += 1;
                stack.pop();
                println!("{:#?}, poppedi:{}, pushedi:{}", stack, poppedi, pushedi);
            }

            pushedi += 1;
            if pushedi < pushed.len(){
                stack.push(pushed[pushedi]);
            }
        }   
        stack.len() == 0
    }
}