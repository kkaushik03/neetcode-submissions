class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<int>> rows(board.size());
vector<unordered_set<int>> cols(board.size()); 
        unordered_set<int> bloc(board.size()); 
        vector<unordered_set<int>> blocks(board.size());

        for (int row = 0; row < board.size() ; row++){
            for (int col = 0; col < board[0].size(); col++ )
            { 
                char c = board[row][col];
                if (c == '.') continue;
                int value = c;

                 if (rows[row].find(value) != rows[row].end())
                    return false; 
                else 
                    rows[row].insert(value);

                 if (cols[col].find(value) != cols[col].end())
                    return false;
                else
                    cols[col].insert(value);
                
                int blocknumber1 = blocknumber(row,col,board.size());
                if(blocks[blocknumber1].find(board[row][col])!=blocks[blocknumber1].end())
                    return false; 
                else 
                    blocks[blocknumber1].insert(board[row][col]);
                
            }
           
        }   
         return true; 
    }

int blocknumber(int row, int col, int boardsize) {
    int blocksize = static_cast<int>(round(sqrt(boardsize)));
    int blockIndex = (row / blocksize) * blocksize + (col / blocksize);
    return blockIndex;
}
};