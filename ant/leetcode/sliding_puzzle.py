import copy
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        puzzle = [[1,2,3],[4,5,0]]
        i, j = 1, 2
        times = 0
        graphs = dict()
        graphs[str(puzzle)] = 0
        stack = list([[i,j,puzzle, times]])
        while stack:
            i,j,puzzle,times = stack.pop(0)
            for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                if i+i_off >=0 and i+i_off < len(puzzle) and j+j_off >=0 and j+j_off<len(puzzle):
                    new = copy.deepcopy(puzzle)
                    new[i][j], new[i + i_off][j+j_off] = new[i + i_off][j+j_off], new[i][j]
                    str_new = str(new)
                    if str_new not in graphs:
                        graphs[str_new] = times + 1
                        stack.append([i + i_off, j+j_off, new, times + 1])
                    else:
                        graphs[str_new] = min(times + 1, graphs[str_new])
            if str(board) in graphs:
                return graphs[str(board)]
        return -1

cases = [
    [[[1,2,3],[4,0,5]], 1],
    [[[1,2,3],[5,4,0]], -1],
    [[[4,1,2],[5,0,3]], 5]
]

for case in cases:
    res = Solution().slidingPuzzle(case[0])
    if res != case[1]:
        raise Exception(case, res)
