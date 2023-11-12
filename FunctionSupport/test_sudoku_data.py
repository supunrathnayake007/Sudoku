
def add_sudoku1_clues(main_list: list) -> list:
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
