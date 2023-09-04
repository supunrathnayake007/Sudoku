from sudokuDb_access import Sudoku_db


while True:
    print()
    print('1 - add new sudoku')
    print('2 - view sudoku')
    print('3 - get sudoku id from name')
    print('Q - for exit')
    print()
    foo = Sudoku_db()
    sudoku_name = ''
    sudoku_data = ''
    user_input = input('>> ')
    if user_input == '1':

        sudoku_name = input('Sudoku name >> ')
        sudoku_data = input('Paste sudoku data >> ')
        foo.insert_data(sudoku_name, sudoku_data)
        # foo.close_db()

    if user_input == '2':
        all_sudoku = foo.view_allSudoku()
        for i in all_sudoku:
            print(str(i[0])+' '+i[1])
        print()
        user_input = input('select a id for transfer (b - for back) >>')
        if user_input == 'b':
            continue

        for i in all_sudoku:
            if str(i[0]) == user_input:
                sudoku_name = i[1]
                sudoku_data = i[2]

        from sqliteAccess import SqliteAccess
        my_sqlite = SqliteAccess()
        s_id = my_sqlite.add_newSudoku(sudoku_name)
        my_sqlite.add_blankSudokuLines(s_id)

        sudoku_dataList = sudoku_data.split(',')
        for i in sudoku_dataList:
            my_sqlite.update_sudokuLine(
                s_id, int(i[0])-1, int(i[1])-1, int(i[2]))

    if user_input == '3':
        user_input = input("    Enter Sudoku name > ")
        sudoku_id = foo.get_sudokuIdFromName(user_input)
        print("Sudoku id is :"+str(sudoku_id))

    if user_input == 'q':
        print('see yaa later!')
        break
