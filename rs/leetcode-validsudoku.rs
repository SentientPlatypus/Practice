impl Solution {

    fn has_duplicate_in_square(board:Vec<Vec<char>>) ->bool{
        for r in (0,9,3) {
            for c in (0,9,3) {
                let nums = Vec::new();
                for i in 0..3 {
                    for j in 0..3 {
                        
                    }
                }
            }
        }
    }



    fn has_duplicate(r:usize, c:usize, val:char, board: Vec<Vec<char>>) ->bool {
        for er in 0..board[r].len() {
            if er != c && board[r][er] == val {
                return false
            }
        }

        for rowindex in 0..board.len() {
            if rowindex != r && board[rowindex][c] == val {
                return false
            }
        }
        true
    }

    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        
    }
}