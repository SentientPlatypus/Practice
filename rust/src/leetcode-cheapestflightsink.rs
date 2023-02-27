impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let infinity:i32 = 10000000;

        let mut prices:Vec<i32> = Vec::new();
        for i in 1..=n {
            prices.push(infinity);
        }

        prices[src as usize] = 0;

        let mut temp:Vec<i32>;

        for i in 0..k + 1 {
            temp = prices.to_vec();

            for edge in &flights {
                let s:i32 = edge[0];
                let d:i32 = edge[1];
                let w:i32 = edge[2];

                if prices[s as usize] != infinity && prices[s as usize] + w < temp[d as usize] {
                    temp[d as usize] = prices[s as usize] + w;
                }
            }

            prices = temp;
        }

        if prices[dst as usize] != infinity {
            return prices[dst as usize]
        }
        -1




    }
}