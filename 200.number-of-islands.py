#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        方法一：深度优先搜索（DFS 沉岛算法，最优解）
        - 思路：
          1. 双重循环遍历网格，当遇到陆地 "1" 时，岛屿数量 ans += 1，并触发 dfs 遍历连通块。
          2. dfs 遍历：
             - 终止条件：坐标越界或当前格子为 "0"（水或已沉没）。
             - 沉岛：将当前格子置为 "0"，避免重复访问和成环。
             - 四向扩散：递归访问上下左右四个相邻格子，将整座岛屿全部沉没。
        - 复杂度：
          - 时间复杂度: O(M * N) —— M、N 为网格行列数，每个格子最多被访问常数次
          - 空间复杂度: O(M * N) —— 最坏情况下（网格全为陆地）递归调用栈深度达 M * N
        """
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return
            elif grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row, col)

        return ans


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
