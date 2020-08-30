class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        
        def check(board,i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!='O':
                return
            board[i][j]= '$'
            check(board, i+1, j)
            check(board, i-1, j)
            check(board, i, j-1)
            check(board, i, j+1)
            
        R=len(board)
        C=len(board[0])
        for i in range(0,C):
            if board[0][i]=='O':
                check(board,0,i)
            if board[R-1][i]=='O':
                check(board,R-1,i)
        
        for i in range(0,R):
            if board[i][0]=='O':
                check(board,i,0)
            if board[i][C-1]=='O':
                check(board,i,C-1)
        
        for i in range(0,R):
            for j in range(0,C):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='$':
                    board[i][j]='O'
        
                    
