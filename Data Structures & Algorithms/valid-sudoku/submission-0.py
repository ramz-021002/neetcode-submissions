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
            sorted_items_row = sorted(count_row.items(), key=lambda x: x[1], reverse=True)
            sorted_items_column = sorted(count_column.items(), key=lambda x: x[1], reverse=True)
            
            for num, freq in sorted_items_row:
                if num != '.' and freq > 1:
                    condition1 = False

            for num, freq in sorted_items_column:
                if num != '.' and freq > 1:
                    condition2 = False
        
        # individual matrix check
        for i in range(0,9,3):
            for j in range(0,9,3):
                matrix = []

                for row in range(i,i+3):
                    for column in range(j,j+3):
                        matrix.append(board[row][column])
                
                count_matrix = Counter(matrix)
                sorted_items_matrix = sorted(count_matrix.items(), key=lambda x: x[1], reverse=True)

                for num, freq in sorted_items_matrix:
                    if num != '.' and freq > 1:
                        condition3 = False

        return (condition1 and condition2 and condition3)

        
            

