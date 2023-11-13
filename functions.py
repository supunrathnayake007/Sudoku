import FunctionSupport.basic_grid_control


def solve_sudoku(my_list: list, testing_mode: bool) -> list:

    possible_values = FunctionSupport.basic_grid_control.new_possible_values_grid()

    while 1 == 1:
        before_count = _count_possibleValues(possible_values)
        # this is where most of the work done
        possible_values = removeIVF_pvTemplate(my_list, possible_values)
        after_count = _count_possibleValues(possible_values)

        my_list = _insert_valuesWTOOPA(
            my_list, possible_values)  # this is a small one
        if before_count == after_count:
            if after_count != 0:
                if testing_mode == True:
                    print("*** Sudoku is not solved!! :( ***")
                    user_input = input(
                        '        press V for View possible Values grid data: ')
                    if user_input.lower() == 'v':
                        print_pvData(my_list, possible_values)

            break
        else:
            before_count = after_count

    return my_list


def guess_possibleValues(main_list: list, row: int, col: int, possible_values: list) -> list:
    if main_list[row][col] > 0:
        return []
    # possible_values = [1,2,3,4,5,6,7,8,9]
    # remove values in selected row
    for i in range(0, 9):
        if i == col:
            continue
        for j in possible_values:
            if j == main_list[row][i]:
                possible_values.remove(j)

    # remove values in selected column
    for i in range(0, 9):
        if i == row:
            continue
        for j in possible_values:
            if j == main_list[i][col]:
                possible_values.remove(j)

    def get_range(index: int) -> list:
        if index < 3 and index > -1:
            return [0, 1, 2]
        elif index < 6 and index > 2:
            return [3, 4, 5]
        else:
            return [6, 7, 8]

    # remove values in 3x3 grid
    row_range = get_range(row)
    col_range = get_range(col)
    for i in row_range:
        for j in col_range:
            for k in possible_values:
                if k == main_list[i][j]:
                    possible_values.remove(k)

    return possible_values


# remove impossible values from the pvTemplate
def removeIVF_pvTemplate(main_list: list, pv_list: list) -> list:
    # new name - filter_possible_values

    # this filter out possible values for selected cell,  it check the row , column and 3x3 cell for filter out
    for row in range(0, 9):
        for col in range(0, 9):
            pv_list[row][col] = guess_possibleValues(
                main_list, row, col, pv_list[row][col])

    # description 1 - this is another major rule or strategy for set the values - when there possible value is uniq to its row , column or 3x3cel
    # even other possible values existed, then that uniq value is the value should be
    #  description 2 - rule-4 set the value when there only one selected pv exist in the raw or column(cell can have more pv but,)
    # selected pv is the only one for the raw or column
    for row in range(0, 9):  # i is row
        for col in range(0, 9):  # j is column
            # k is selected possible value itself
            for possible_value in pv_list[row][col]:

                # check is k available in other cells pv
                is_available = False

                # this check the row for uniq value (only column index change)
                for l in range(0, 9):  # l is column
                    if l == col:
                        continue
                    for m in pv_list[row][l]:  # m is a possible value
                        if possible_value == m:
                            is_available = True
                            break
                    if is_available:
                        break

                if is_available == False:
                    pv_list[row][col] = [possible_value]
                    break
                else:
                    is_available = False
                    for l in range(0, 9):
                        if l == i:
                            continue
                        for m in pv_list[l][col]:
                            if possible_value == m:
                                is_available = True
                                break
                        if is_available:
                            break

                if is_available == False:
                    pv_list[row][col] = [possible_value]
                    break
                else:
                    is_available = False
                    row_range = _get_range(row)
                    col_range = _get_range(col)

                    for l in row_range:
                        for m in col_range:
                            if l == row and m == col:
                                continue
                            for n in pv_list[l][m]:
                                if possible_value == n:
                                    is_available = True
                                    break
                            if is_available:
                                break
                        if is_available:
                            break

                    if is_available == False:
                        pv_list[row][col] = [possible_value]
                        break

    # for i in range(0, 9):
    #     have_values = 0
    #     for j in range(0, 9):
    #         if main_list[i][j] > 0:
    #             have_values = have_values+1
    #             continue
    #         elif have_values==8:

    return pv_list


def _count_possibleValues(pv_list: list) -> int:
    count = 0
    for i in range(0, 9):
        for j in range(0, 9):
            for k in pv_list[i][j]:
                if k > 0:
                    count = count+1
    return count


def _insert_valuesWTOOPA(main_list: list, pv_list: list) -> list:
    # insert values When There Only One Possible Value Available
    # new name  - insert_single_values
    for i in range(0, 9):
        for j in range(0, 9):
            if len(pv_list[i][j]) == 1:
                main_list[i][j] = pv_list[i][j][0]
    return main_list


def _get_range(index: int) -> list:
    # give the given index of 3x3 grid range - improve the description
    if index < 3 and index > -1:
        return [0, 1, 2]
    elif index < 6 and index > 2:
        return [3, 4, 5]
    else:
        return [6, 7, 8]


# my_list = create_blankGrid()
# my_list = add_clues(my_list)
# print_myGrid(my_list)

# pv_list = generate_pvTemplate()
# my_list = solve_sudoku(my_list,pv_list)


# print("")
# print_myGrid(my_list)
