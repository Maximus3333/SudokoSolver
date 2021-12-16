def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rowcounter = 0
    sub_boxes_and_cell_values = subboxes(board)
    sub_box_dict = sub_boxes_and_cell_values[0]
    cells = sub_boxes_and_cell_values[1]
    columnboard = column_board(board)
    cell_coordinates = ""
    rowcounter = 0
    columncounter = 0
    for cell_coordinates_and_sub_box_coordinates_key in cells:
        cell_value = cells[cell_coordinates_and_sub_box_coordinates_key][0]
        sub_box_coordinates = cells[cell_coordinates_and_sub_box_coordinates_key][1]
        if cell_value == '.':
            values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for values_in_sub_box in sub_box_dict[sub_box_coordinates]:
                if values_in_sub_box in values:
                    values.remove(values_in_sub_box)
            row = board[int(cell_coordinates_and_sub_box_coordinates_key[0])]
            column = columnboard[int(cell_coordinates_and_sub_box_coordinates_key[2])]
            for row_values in row:
                if row_values in values:

    for sub_box_key in subbox_dict:
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for cell in subbox_dict[sub_box_key]:
            if columncounter >= int(sub_box_key[2]):
                columncounter = 0
                rowcounter += 1
            cell_coordinates = "" + rowcounter + "x" + "" + columncounter
            if cell == '.':
                if cell_coordinates not in possible_values_in_cells.keys():

            possible_values_in_cells[cell_coordinates] = []
            possible_values_in_cells[cell_coordinates] += values
            if int(cell) in values:

            if cell == '.':

                if int(cell) in values:
                    values.remove(int(cell))
                for columns in

            columncounter += 1




        if cell_coordinates not in possible_values_in_cells.keys():
            values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            columncounter = 0
            for cell in row:
                if cell == '.':

                    if int(cell) in values:
                        values.remove(int(cell))
                    for columns in

        cell_coordinates = "" + rowcounter + "x" + "" + columncounter
        possible_values_in_cells[cell_coordinates] = []
        possible_values_in_cells[cell_coordinates] += values

        columncounter += 1
    rowcounter += 1

def subboxes(rowboard):
    subbox_dict = {}
    cell_dict = {}
    rowcounter = 0
    currentkey = ""
    for row in rowboard:
        columncounter = 0
        for cell in row:
            if columncounter % 3 == 0 and rowcounter % 3 == 0:
                subbox = [cell]
                key = ""+ str(rowcounter+3) + "x" + str(columncounter+3)
                subbox_dict[key] = subbox
                currentkey = key
            elif currentkey in subbox_dict.keys():
                for key in subbox_dict.keys():
                    if int(key[0])>rowcounter and rowcounter >= int(key[0])-3 and int(key[2])>columncounter and int(key[2])-3<=columncounter:
                        currentkey = key
                subbox = subbox_dict[currentkey]
                subbox.append(cell)
            cell_coordinates = "" + str(rowcounter) + "x" + "" + str(columncounter)
            # print(cell_coordinates)
            cell_dict[cell_coordinates] = [cell, currentkey]
            columncounter+=1
        rowcounter+=1
    # print(cell_dict)
    return subbox_dict, cell_dict

def column_board(rowboard):
    new_list = []
    rowcounter = 0
    for row in rowboard:
        columncounter = 0
        for cell in row:
            if rowcounter == 0:
                column = [cell]
                new_list.append(column)
            else:
                column = new_list[columncounter]
                column.append(cell)
            columncounter+=1
        rowcounter+=1

    return new_list

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# column_board(board)
print(subboxes(board))