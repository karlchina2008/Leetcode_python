class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:return
        m,n=len(board),len(board[0])
        find=[[(j,i) for i in range(n)] for j in range(m)]
        #print find
        size=[ [board[j][i]=='O' for i in range(n)] for j in range(m)]
        
        def findroot(a,b):
            t=find[a][b]
            while t!=find[t[0]][t[1]]:
                find[a][b]=find[t[0]][t[1]]
                a,b=find[a][b]
                t=find[a][b]
            return t
        def connect(t_1,t_2):
            if t_1!=t_2:
                if t_1[0]==0 or t_1[0]==m-1 or t_1[1]==0 or t_1[1]==n-1:
                    find[t_2[0]][t_2[1]]=t_1
                    size[t_1[0]][t_1[1]]+=size[t_2[0]][t_2[1]]
                elif t_2[0]==0 or t_2[0]==m-1 or t_2[1]==0 or t_2[1]==n-1:
                    find[t_1[0]][t_1[1]]=t_2
                    size[t_2[0]][t_2[1]]+=size[t_1[0]][t_1[1]]
                elif size[t_1[0]][t_1[1]]>=size[t_2[0]][t_2[1]]:
                    find[t_2[0]][t_2[1]]=t_1
                    size[t_1[0]][t_1[1]]+=size[t_2[0]][t_2[1]]
                else:
                    find[t_1[0]][t_1[1]]=t_2
                    size[t_2[0]][t_2[1]]+=size[t_1[0]][t_1[1]]
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if i+1<m and board[i+1][j]=='O':
                        temp=findroot(i,j)
                        temp_1=findroot(i+1,j)
                        connect(temp,temp_1)
                    if j+1<n and board[i][j+1]=='O':
                        temp=findroot(i,j)
                        temp_1=findroot(i,j+1)
                        connect(temp,temp_1)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    x,y=findroot(i,j)
                    if 0<x<m-1 and 0<y<n-1:
                        board[i][j]='X'
