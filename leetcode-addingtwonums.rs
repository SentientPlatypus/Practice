impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match (l1, l2) {
            (None, None) => None,
            (Some(n), None) | (None, Some(n)) => Some(n),
            (Some(n1), Some(n2)) => {
                let sum = n1.val + n2.val;
                let c = sum / 10;
                let cnode = if c == 0 {None} else {Some(Box::new(ListNode::new(c)))};
                Some(Box::new(ListNode{
                    val: sum % 10, 
                    next: Solution::add_two_numbers(
                            Solution::add_two_numbers(
                                n1.next,
                                cnode
                            )
                        ,
                        n2.next
                    )
                }))
            }
        }
    }
}