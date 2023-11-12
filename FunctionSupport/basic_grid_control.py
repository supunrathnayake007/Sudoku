def create_blank_grid() -> list:
    # this create 9x9 list with 0s
    # old name - create_blankGrid
    main_list = []
    for i in range(0, 9):
        main_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    return main_list


def all_possible_values_grid() -> list:
    # this is a 3d(9x9x9) list contains all possible values for each cell in sudoku grid
    # old name - generate_pvTemplate
    pv_list = []
    for i in range(0, 9):
        pv_list.append([])
        for j in range(0, 9):
            pv_list[i].append([1, 2, 3, 4, 5, 6, 7, 8, 9])

    return pv_list


def tuple_to_List_twoD(my_tuple: tuple) -> list:
    # tupleOfTuplesTo_listOfLists -old name
    main_list = []
    for i in range(0, 9):
        sub_list = []
        for j in range(0, 9):
            sub_list.append(my_tuple[i][j])
        main_list.append(sub_list)

    return main_list


# below is console related functions
def print_grid(main_list: list):  # in console
    # old name -print_myGrid
    # this print the 9x9 list like sudoku grid in console
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


def print_possible_values(main_list: list, pv_list: list):
    # old name - print_pvData
    # this print possible value list in basic way
    for i in range(0, 9):
        print('row:'+str(i))
        for j in range(0, 9):
            if main_list[i][j] > 0:
                continue
            print('     col:'+str(j)+' val:' + ' pv:'+str(pv_list[i][j]))
        print()
