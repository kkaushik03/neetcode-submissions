class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        col_len=len(board[0])
        row_len=len(board)
        solution=False
        visited = set()

        def helper(curr_word,curr_row,curr_col,curr_index_matcher): 
            if curr_index_matcher == len(word): 
                solution=True
                return True
            if curr_row < 0 or curr_row >= row_len or curr_col < 0 or curr_col >= col_len:
                return False
            if (curr_row, curr_col) in visited or board[curr_row][curr_col] != word[curr_index_matcher]:
                return False

            visited.add((curr_row, curr_col))

            for dr,dc in directions:
                nr = dr + curr_row
                nc = dc + curr_col
                if helper(curr_word,nr,nc,curr_index_matcher+1):
                    solution=True
                    return True
            visited.remove((curr_row, curr_col))
            return False
        # Add loop before helper call:
        for i in range(row_len):
            for j in range(col_len):
                if helper("", i, j, 0):
                    return True
        return False

            