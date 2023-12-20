impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        if prices.len() < 2 {
            return money;
        }

        let mut h = std::i32::MAX;
        let mut sh = std::i32::MAX;

        for i in 0..prices.len() {
            if prices[i] < h {
                sh = h;
                h = prices[i];
            } else if prices[i] < sh {
                sh = prices[i];
            }
        }

        if money - h - sh < 0 {
            return money;
        }
        money - h - sh
    }
}
