class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0]*(len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(matrix[0])):
            matrix[0][i] = i
        
        for i in range(len(matrix)):
            matrix[i][0] = i

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                del_cost = matrix[i - 1][j] + 1
                ins_cost = matrix[i][j-1] + 1
                replace_cost = matrix[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    replace_cost += 1

                matrix[i][j] = min(del_cost, ins_cost, replace_cost)

        return matrix[-1][-1]

if __name__ != "main":
    sol = Solution()
    cost = sol.minDistance("horse", "ros")
    print(cost)
    cost = sol.minDistance("intention", "execution")
    print(cost)
