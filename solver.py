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
    recurse = 0
    first_inst = 1
    while recurse == 1 or first_inst == 1:
        first_inst = 0
        recurse = 0
        for cell_coordinates_and_sub_box_coordinates_key in cells:
            cell_value = cells[cell_coordinates_and_sub_box_coordinates_key][0]
            sub_box_coordinates = cells[cell_coordinates_and_sub_box_coordinates_key][1]
            if cell_value == '.':
                values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            elif type(cell_value) == list:
                values = cell_value
                # print(values, cell_coordinates_and_sub_box_coordinates_key)
            if cell_value == '.' or type(cell_value) == list:
                recurse = 1
                # print(cell_value, cell_coordinates_and_sub_box_coordinates_key)
                # print(sub_box_dict[sub_box_coordinates])
                for values_in_sub_box in sub_box_dict[sub_box_coordinates]:
                    # print(values_in_sub_box[0])
                    value = values_in_sub_box[0]
                    # val_pos = values_in_sub_box[1]
                    if value != ".":
                        value = int(value)
                        if value in values:
                            # print(value)
                            values.remove(value)
                            # print(values, cell_coordinates_and_sub_box_coordinates_key)
                row = board[int(cell_coordinates_and_sub_box_coordinates_key[0])]
                column = columnboard[int(cell_coordinates_and_sub_box_coordinates_key[2])]
                for row_values in row:
                    if row_values != ".":
                        row_values = int(row_values)
                        if row_values in values:
                            values.remove(row_values)
                            # print(row_values)
                for column_values in column:
                    # print(column_values)
                    if column_values != ".":
                        column_values = int(column_values)
                        if column_values in values:
                            values.remove(column_values)
                            # print(column_values)
                if len(values) == 1:
                    cells[cell_coordinates_and_sub_box_coordinates_key][0] = values[0]
                    # print(board[int(cell_coordinates_and_sub_box_coordinates_key[0])][int(cell_coordinates_and_sub_box_coordinates_key[2])])
                    # print(row[int(cell_coordinates_and_sub_box_coordinates_key[0])][int(cell_coordinates_and_sub_box_coordinates_key[2])])
                    board[int(cell_coordinates_and_sub_box_coordinates_key[0])][int(cell_coordinates_and_sub_box_coordinates_key[2])] = str(values[0])
                    columnboard[int(cell_coordinates_and_sub_box_coordinates_key[2])][int(cell_coordinates_and_sub_box_coordinates_key[0])] = str(values[0])
                    count = 0
                    for values_in_sub_box in sub_box_dict[sub_box_coordinates]:
                        val_pos = values_in_sub_box[1]
                        # print(values_in_sub_box)
                        if val_pos == cell_coordinates_and_sub_box_coordinates_key:
                        #     # print(sub_box_dict[sub_box_coordinates][count])
                            sub_box_dict[sub_box_coordinates][count][0] = str(values[0])
                            # print(sub_box_dict[sub_box_coordinates][count])
                        #     # print(sub_box_dict[sub_box_coordinates][count])
                        count+=1
                else:
                    cells[cell_coordinates_and_sub_box_coordinates_key][0] = values

def subboxes(rowboard):
    subbox_dict = {}
    cell_dict = {}
    rowcounter = 0
    currentkey = ""
    for row in rowboard:
        columncounter = 0
        for cell in row:
            cell_coordinates = "" + str(rowcounter) + "x" + "" + str(columncounter)
            if columncounter % 3 == 0 and rowcounter % 3 == 0:
                subbox = [[cell, cell_coordinates]]
                key = ""+ str(rowcounter+3) + "x" + str(columncounter+3)
                subbox_dict[key] = subbox
                currentkey = key
            elif currentkey in subbox_dict.keys():
                for key in subbox_dict.keys():
                    if int(key[0])>rowcounter and rowcounter >= int(key[0])-3 and int(key[2])>columncounter and int(key[2])-3<=columncounter:
                        currentkey = key
                subbox = subbox_dict[currentkey]
                subbox.append([cell, cell_coordinates])
            # print(cell_coordinates)
            cell_dict[cell_coordinates] = [cell, currentkey]
            columncounter+=1
        rowcounter+=1
    # print(subbox_dict)
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
# print(subboxes(board)[0])
solveSudoku(board)
# subboxes(board)