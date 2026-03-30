class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0, len(matrix) - 1

        while left <= right:

            mid = (left+right) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:

                left, right = 0, len(matrix[mid]) - 1

                while left <= right:

                    mid2 = (left+right) // 2

                    if target == matrix[mid][mid2]:

                        return True

                    elif target > matrix[mid][mid2]:

                        left = mid2+1

                    else:

                        right = mid2-1

                return False

            elif target > matrix[mid][len(matrix[mid])-1]:

                left = mid + 1

            else:

                right = mid -1


        return False
        