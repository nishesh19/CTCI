class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        result = []
        row_size = len(matrix)
        col_size = len(matrix[0])

        i_range = [0, row_size]
        j_range = [0, col_size]

        # start = (i_range[0],j_range[0])

        while (i_range[0] < i_range[1]) and (j_range[0] < j_range[1]):
            i, j = i_range[0], j_range[0]

            while j < j_range[1]:
                result.append(matrix[i][j])
                j += 1

            j = j_range[1] - 1
            i += 1

            while i < i_range[1]:
                result.append(matrix[i][j])
                i += 1

            i = i_range[1] - 1
            j -= 1

            while (j >= j_range[0] and j == 0) or (j > j_range[0]):
                result.append(matrix[i][j])
                j -= 1

            j = j_range[0]
            i -= 1

            while i > i_range[0]:
                result.append(matrix[i][j])
                i -= 1

            i_range[0] += 1
            j_range[0] += 1

            i_range[1] -= 1
            j_range[1] -= 1

        return result


if __name__ == '__main__':
    sol = Solution()

    # matrix = [
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10],
    #     [11, 12, 13, 14, 15],
    #     [16, 17, 18, 19, 20],
    #     [21, 22, 23, 24, 25],
    #     [26, 27, 28, 29, 30]
    # ]
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.spiralOrder(matrix2))
