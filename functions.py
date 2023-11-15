import FunctionSupport.basic_grid_control


def solve_sudoku(my_list: list, testing_mode: bool) -> list:

    possible_values = FunctionSupport.basic_grid_control.new_possible_values_grid()

    while 1 == 1:
        before_count = _count_possible_values(possible_values)
        possible_values = remove_unnecessary_possible_values(
            my_list, possible_values)
        # this is where most of the work done
        possible_values = removeIVF_pvTemplate(my_list, possible_values)
        after_count = _count_possible_values(possible_values)

        my_list = _insert_valuesWTOOPA(
            my_list, possible_values)  # this is a small one
        if before_count == after_count:
            if after_count != 0:
                if testing_mode == True:
                    print("*** Sudoku is not solved!! :( ***")
                    FunctionSupport.basic_grid_control.print_possible_values(
                        my_list, possible_values)
                    print("         suggest a value")
                    # if user_input.lower() == 'v':

                    if user_input.lower() == 's':
                        row_s = input('             Row index:')
                        col_s = input('             column index:')
                        value_s = input('             Value:')
                        my_list[int(row_s)][int(col_s)] = int(value_s)
                        continue

                return my_list

            break
        else:
            before_count = after_count  # no need now

    return my_list


def remove_unnecessary_possible_values(main_list: list, possible_values: list) -> list:
    # old name - guess_possibleValues
    # this method good to call when after value added to the main grid or after new possible value list created
    # in this method we are going to clean the possible value list according to main grid
    # like if there value in the main grid then that value doesn't need to be possible value in the entire row column and 3x3 cell
    # its like a cleaning remaining unnecessary possible values

    # this is like the step one to remove unnecessary possible values

    for row in range(0, 9):
        for col in range(0, 9):
            # pv_list[row][col] = guess_possibleValues(
            #     main_list, row, col, pv_list[row][col])

            # in here if there value in main grid then we gonna skip that cell
            # because it already have a value no need any checking
            # to think - we also can remove all the possible values, may be assign 0
            if main_list[row][col] > 0:
                # this will remove unnecessary possible values then there already certain values exist
                possible_values[row][col] = []
                continue

            # this check the entire column and remove unnecessary possible values
            for i in range(0, 9):  # i is column index
                if i == col:  # this prevent checking its own cell - improve this hard to understand
                    # this might not need, not sure , keeping it seems no harm
                    continue
                for j in possible_values[row][col]:  # j is possible value
                    if j == main_list[row][i]:
                        possible_values[row][col].remove(j)

            # this check the entire row and remove unnecessary possible values, work same like above
            for i in range(0, 9):  # i is row index
                if i == row:
                    continue
                for j in possible_values[row][col]:
                    if j == main_list[i][col]:
                        possible_values[row][col].remove(j)

            # this check the entire 3x3 cell and remove unnecessary possible values
            row_range = _get_range(row)
            col_range = _get_range(col)
            for i in row_range:
                for j in col_range:
                    for k in possible_values[row][col]:
                        if k == main_list[i][j]:
                            possible_values[row][col].remove(k)

    return possible_values


# remove impossible values from the pvTemplate
def removeIVF_pvTemplate(main_list: list, pv_list: list) -> list:
    # new name - filter_possible_values

    # description 1 - this is another major rule or strategy for set the values - when there possible value is uniq to its row , column or 3x3cel
    # even other possible values existed, then that uniq value is the value should be
    #  description 2 - rule-4 set the value when there only one selected pv exist in the raw or column(cell can have more pv but,)
    # selected pv is the only one for the raw or column
    for row in range(0, 9):  # i is row
        for col in range(0, 9):  # j is column

            if len(pv_list[row][col]) == 1:
                continue
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

                # if selected possible value doesn't exist in the other cells on the row, remove other possible values in that cell
                # that leave one possible values and that will be the certain value for the grid - [may improve need to understand]
                # after selecting the certain value, possible value loop will brake here and not going further
                if is_available == False:
                    pv_list[row][col] = [possible_value]
                    break

                # else - if possible value exist in the row, "is_available" value reset for false and proceed to next step
                # which is gonna check column
                is_available = False

                # this is same like above loop but this checks the entire column instead the row.
                # if there no possible value like the selected one "is_available" value remain false
                # it means selected possible value is the certain value
                for l in range(0, 9):
                    if l == row:
                        continue
                    for m in pv_list[l][col]:
                        if possible_value == m:
                            is_available = True
                            break
                    if is_available:
                        break

                # this is like above line 108
                if is_available == False:
                    pv_list[row][col] = [possible_value]
                    break

                # above we check the row then column now we gonna check 3x3 cell
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


def _count_possible_values(pv_list: list) -> int:
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
    # give the range of given index for 3x3 grid
    # this works well with row and column, coz there are both same
    if index < 3 and index > -1:
        return [0, 1, 2]
    elif index < 6 and index > 2:
        return [3, 4, 5]
    else:
        return [6, 7, 8]


def _check_main_list_complete(main_list: list) -> bool:
    # this method to check actually main list got fixed
    # because possible values list count can goto 0 with bad suggestions and still main list can be not fixed
    # so this check the main list is there any o values, if there is its not fixed , if there isn't its fixed

    for row in range(0, 9):
        for col in range(0, 9):
            if main_list[row][col] == 0:
                return False
    return True


# my_list = create_blankGrid()
# my_list = add_clues(my_list)
# print_myGrid(my_list)

# pv_list = generate_pvTemplate()
# my_list = solve_sudoku(my_list,pv_list)


# print("")
# print_myGrid(my_list)


def lets_brute_force(main_list: list, possible_values: list) -> list:
    # in this list first (0) index is like column heder in table
    # and this is where im gonna track every step
    _brute_history = ["step_id", "main_list", "possible_values",
                      "suggesting value", "row_index", "column_index"]
    _step_id = 0

    while 1 == 1:

        _track_back = False

        for row in range(0, 9):
            for col in range(0, 9):

                for possible_value in possible_values[row][col]:
                    if main_list[row][col] == 0:
                        _step_id = _step_id+1  # this will increase the step number
                        _brute_history.append(
                            [_step_id, main_list, possible_values, possible_value, row, col])  # saving data before make change

                        # making the suggestion without knowing right or wrong
                        main_list[row][col] = possible_value
                        # remove other possible values , those doesn't matter anymore
                        possible_values[row][col] = possible_value
                        possible_values = remove_unnecessary_possible_values(
                            main_list, possible_values)  # cleaning up other possible values according to our change

                    break  # need to run one time

        if (_track_back):
            for history in _brute_history:
                break

        # main while loop stops only when possible values count become 0
        # this should be the end of the this method
        if (_count_possible_values(possible_value) == 0):
            return main_list

    return [0]
