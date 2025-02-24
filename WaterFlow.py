class Solution:
    def pacificAtlantic(self, heights):
        '''
        for every point 
            canFlowPacific 
            canFlowAtlantic 

        canFlowPacific(i,j)
            if i == 0 or j == 0:
                return True 
            else:
                # blocked dont traverse
                if (i != 0 and heights[i-1][j] > heights[i][j]) and (j != 0 and heights[i][j-1] > heights[i][j]):
                    return False
                else:
                    top = None
                    left = None 
                    if i != 0:
                        top = canFlowPacific(i-1,j)
                    if j != 0:
                        left = canFlowPacific(i,j-1)
                    return top or left
        '''

        rows = len(heights)
        cols = len(heights[0])
        res = []
        pacificDp = [[-1 for _ in range(cols)] for _ in range(rows)]
        atlanticDp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def canFlowPacific(row,col):
            if row == 0 or col == 0:
                return True 
            if pacificDp[row][col] != -1:
                return pacificDp[row][col]
            else:
                # blocked 
                if(row != 0 and heights[row-1][col] > heights[row][col]) and (col != 0 and heights[row][col-1] > heights[row][col]):
                    pacificDp[row][col] = False 
                    return pacificDp[row][col]
                else:
                    top = None 
                    left = None 
                    if row != 0:
                        top = canFlowPacific(row-1,col)
                    if col != 0:
                        left = canFlowPacific(row,col-1)
                    pacificDp[row][col] = top or left 
                    return pacificDp[row][col]
        
        def canFlowAtlantic(row,col):
            if row == rows-1 or col == cols-1:
                return True 
            if atlanticDp[row][col] != -1:
                return atlanticDp[row][col]
            else:
                # blocked 
                if(row != rows-1 and heights[row+1][col] > heights[row][col]) and (col != cols-1 and heights[row][col+1] > heights[row][col]):
                    atlanticDp[row][col] = False 
                    return atlanticDp[row][col]
                else:
                    right = None 
                    bottom = None 
                    if row != rows-1:
                        right = canFlowAtlantic(row+1,col)
                    if col != cols-1:
                        bottom = canFlowAtlantic(row,col+1)
                    atlanticDp[row][col] = right or bottom
                    return atlanticDp[row][col]

        for row in range(rows):
            for col in range(cols):
                pacific = canFlowPacific(row,col)
                atlantic = canFlowAtlantic(row,col)
                if(pacific and atlantic):
                    res.append([row,col])
        return res

arr = [[1,2,3],[8,9,4],[7,6,5]]
print(Solution().pacificAtlantic(arr))