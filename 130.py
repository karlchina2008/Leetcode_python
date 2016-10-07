class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:return
        m,n=len(board),len(board[0])
        save=[ij for k in range(max(m,n)) for ij in ((0,k),(m-1,k),(k,0),(k,n-1))]
        while len(save)>0:
            i,j=save.pop()
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='Y'
                save+=((i+1,j),(i,j+1),(i-1,j),(i,j-1))# or save.append((i,j))
        board[:] = [['XO'[c == 'Y'] for c in row] for row in board]
 
