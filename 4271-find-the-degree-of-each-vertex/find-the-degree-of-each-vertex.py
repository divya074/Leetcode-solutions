class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        arrlen = len(matrix)
        ans = [0]*arrlen
        for i in range(arrlen):
            for j in matrix[i]:
                ans[i] += j

        return ans
        