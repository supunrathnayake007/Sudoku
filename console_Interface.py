import functions
import FunctionSupport.basic_grid_control
import FunctionSupport.test_sudoku_data

from DBAccess.sqliteAccess import SqliteAccess
foo = SqliteAccess()
foo.create_db()
#
print()
print('******************************************************')
print('*********Welcome to Sudoku solving program************')
print('******************************************************')

while True:
    print()
    print('type: ')
    print('A - Add new sudoku for solve ')
    print('V - load old sudoku')
    print('Q - for quit the program')
    print('******************************************************')
    answer = input('>> ')
    print()
    if answer.lower() == 'q':
        break

    if answer.lower() == 'a':
        s_name = input('    Type a name >> ')
        print('    Please add clues!')
        print('    D - for finish')
        s_id = foo.add_newSudoku(s_name)
        foo.add_blankSudokuLines(s_id)

        # foo.update_sudokuLine(s_id,2,2,9)
        while True:
            row = input('    row >> ')
            if row.lower == 'd':
                break
            col = input('    column >> ')
            value = input('    value >> ')
            if value.lower == 'd':
                break
            foo.update_sudokuLine(s_id, int(row)-1, int(col)-1, int(value))
            print()

    if answer.lower() == 'fi':
        r = input('    This is factory insert. want to proceed (y/n)?')
        if r.lower() == 'y':
            myList = FunctionSupport.basic_grid_control.create_blank_grid()
            myList = FunctionSupport.add_clues(myList)
            foo.insert_sudokuFromList(myList, 'first_sudoku')

    if answer.lower() == 'v':
        while True:
            sudoku = foo.get_AllSudoku()
            for i in sudoku:
                print(i)

            s_id = input('    enter sudoku number >> ')
            print()
            sudokuData = foo.get_sudokuFromLines(s_id)
            my_list = FunctionSupport.basic_grid_control.tuple_to_List_twoD(
                sudokuData)
            FunctionSupport.basic_grid_control.print_grid(my_list)
            print()
            print('     S - for solve')
            print('     B - Back')
            print('     M - Main menu')
            print()
            user_input = input('     >> ')
            if user_input.lower() == 's':
                _result = functions.solve_sudoku(my_list)

                if _result['is_solved']:
                    print('SODOKU is Solved !!')
                    print()
                else:
                    print('SODOKU is failed to Solved !!')
                    FunctionSupport.basic_grid_control.print_possible_values(
                        _result['possible_values'])
                    print()
                FunctionSupport.basic_grid_control.print_grid(
                    _result['main_grid'])

                print()
                print('     B - Back')
                print('     M - Main menu')
            if user_input.lower() == 'm':
                break
            if user_input.lower() == 'b':
                continue

foo.close_db()
