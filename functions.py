
def create_blankGrid() -> list:
    main_list = []
    for i in range(0, 9):
        main_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    return main_list


def tupleOfTuplesTo_listOfLists(my_tuple: tuple) -> list:

    main_list = []
    for i in range(0, 9):
        sub_list = []
        for j in range(0, 9):
            sub_list.append(my_tuple[i][j])
        main_list.append(sub_list)

    return main_list


def print_myGrid(main_list: list):
    i = 0
    while i < 9:
        j = 0
        line_str = ""
        while j < 9:
            line_str = line_str + str(main_list[i][j])
            if j == 2 or j == 5 or j == 8:
                line_str = line_str + "  "
            else:
                line_str = line_str + ", "
            j = j+1
        if i == 3 or i == 6 or i == 9:
            print("")
        print(line_str)
        i = i+1


def add_clues(main_list: list) -> list:
    main_list[0][3] = 9
    main_list[1][0] = 2
    main_list[1][2] = 4
    main_list[1][4] = 5
    main_list[1][6] = 8
    main_list[1][8] = 7
    main_list[2][1] = 7
    main_list[2][4] = 8
    main_list[2][5] = 3
    main_list[2][7] = 4
    main_list[3][0] = 8
    main_list[3][6] = 9
    main_list[4][0] = 9
    main_list[4][1] = 1
    main_list[4][6] = 3
    main_list[4][7] = 5
    main_list[5][0] = 4
    main_list[5][2] = 2
    main_list[5][6] = 6
    main_list[5][8] = 8
    main_list[6][3] = 7
    main_list[7][0] = 1
    main_list[7][2] = 8
    main_list[7][4] = 9
    main_list[7][6] = 7
    main_list[7][8] = 6
    main_list[8][1] = 3
    main_list[8][4] = 1
    main_list[8][5] = 2
    main_list[8][7] = 9

    return main_list


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


def generate_pvTemplate() -> list:
    # Generate passible value template list
    pv_list = []
    for i in range(0, 9):
        pv_list.append([])
        for j in range(0, 9):
            pv_list[i].append([1, 2, 3, 4, 5, 6, 7, 8, 9])

    return pv_list

# insert values When There Only One Possible Value Available


def insert_valuesWTOOPA(main_list: list, pv_list: list) -> list:
    # insert values When There Only One Possible Value Available
    for i in range(0, 9):
        for j in range(0, 9):
            if len(pv_list[i][j]) == 1:
                main_list[i][j] = pv_list[i][j][0]
    return main_list

# remove impossible values from the pvTemplate


def removeIVF_pvTemplate(main_list: list, pv_list: list) -> list:
    def get_range(index: int) -> list:
        if index < 3 and index > -1:
            return [0, 1, 2]
        elif index < 6 and index > 2:
            return [3, 4, 5]
        else:
            return [6, 7, 8]

    for i in range(0, 9):
        for j in range(0, 9):
            pv_list[i][j] = guess_possibleValues(
                main_list, i, j, pv_list[i][j])

    # rule-4 set the value when there only one selected pv exist in the raw or column(cell can have more pv but,)
    # selected pv is the only one for the raw or column
    for i in range(0, 9):  # i is row
        for j in range(0, 9):  # j is column
            for k in pv_list[i][j]:  # k is selected pv itself

                # check is k available in other cells pv
                is_available = False

                for l in range(0, 9):  # l is column
                    if l == j:
                        continue
                    for m in pv_list[i][l]:  # m is a pv
                        if k == m:
                            is_available = True
                            break
                    if is_available:
                        break

                if is_available == False:
                    pv_list[i][j] = [k]
                    break
                else:
                    is_available = False
                    for l in range(0, 9):
                        if l == i:
                            continue
                        for m in pv_list[l][j]:
                            if k == m:
                                is_available = True
                                break
                        if is_available:
                            break

                if is_available == False:
                    pv_list[i][j] = [k]
                    break
                else:
                    is_available = False
                    row_range = get_range(i)
                    col_range = get_range(j)

                    for l in row_range:
                        for m in col_range:
                            if l == i and m == j:
                                continue
                            for n in pv_list[l][m]:
                                if k == n:
                                    is_available = True
                                    break
                            if is_available:
                                break
                        if is_available:
                            break

                    if is_available == False:
                        pv_list[i][j] = [k]
                        break

    # for i in range(0, 9):
    #     have_values = 0
    #     for j in range(0, 9):
    #         if main_list[i][j] > 0:
    #             have_values = have_values+1
    #             continue
    #         elif have_values==8:

    return pv_list


def solve_sudoku(my_list: list, pv_list: list, testing_mode: bool) -> list:

    def count_possibleValues(pv_list: list) -> int:
        count = 0
        for i in range(0, 9):
            for j in range(0, 9):
                for k in pv_list[i][j]:
                    if k > 0:
                        count = count+1
        return count

    key_value = count_possibleValues(pv_list)
    while 1 == 1:
        pv_list = removeIVF_pvTemplate(my_list, pv_list)
        key = count_possibleValues(pv_list)

        my_list = insert_valuesWTOOPA(my_list, pv_list)
        if key_value == key:
            if key != 0:
                if testing_mode == True:
                    print("*** Sudoku is not solved!! :( ***")
                    user_input = input(
                        '        press V for View possible Values grid data: ')
                    if user_input.lower() == 'v':
                        print_pvData(my_list, pv_list)

            break
        else:
            key_value = key

    return my_list


def print_pvData(main_list: list, pv_list: list):
    for i in range(0, 9):
        print('row:'+str(i))
        for j in range(0, 9):
            if main_list[i][j] > 0:
                continue
            print('     col:'+str(j)+' val:' + ' pv:'+str(pv_list[i][j]))
        print()


# my_list = create_blankGrid()
# my_list = add_clues(my_list)
# print_myGrid(my_list)

# pv_list = generate_pvTemplate()
# my_list = solve_sudoku(my_list,pv_list)


# print("")
# print_myGrid(my_list)
