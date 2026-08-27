class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        condition1 = True
        condition2 = True
        condition3 = True
        # Row checking and Column checks
        for i in range(9):
            row = board[i]
            column = [row[i] for row in board]
            count_row = Counter(row)
            count_column = Counter(column)
            
            for num, freq in count_row.items():
                if num != '.' and freq > 1:
                    return False

            for num, freq in count_column.items():
                if num != '.' and freq > 1:
                    return False
        
        # individual matrix check
        for i in range(0,9,3):
            for j in range(0,9,3):
                matrix = []

                for row in range(i,i+3):
                    for column in range(j,j+3):
                        matrix.append(board[row][column])
                
                count_matrix = Counter(matrix)

                for num, freq in count_matrix.items():
                    if num != '.' and freq > 1:
                        return False


        return True

        
            

