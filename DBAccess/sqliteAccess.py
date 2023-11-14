import sqlite3


class SqliteAccess:
    def __init__(self):
        self.conn = sqlite3.connect('DBAccess/data.db')
        self.c = self.conn.cursor()
        self.create_db()

    def close_db(self):
        self.conn.close()

    def create_db(self):

        self.c.execute("""CREATE Table IF NOT EXISTS sudoku (
              id integer UNIQUE,
              name text
            )""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS sudokuLines(
              sudokuId integer,
              row integer,
              col1 integer,
              col2 integer,
              col3 integer,
              col4 integer,
              col5 integer,
              col6 integer,
              col7 integer,
              col8 integer,
              col9 integer
    )""")
        self.conn.commit()

    def get_latestSudokuId(self) -> int:
        self.c.execute("SELECT MAX(id) FROM sudoku")
        result = self.c.fetchone()
        if result[0] == None:
            return 0
        return int(result[0])

    def add_newSudoku(self, sudoku_name) -> int:
        id = 0
        id = self.get_latestSudokuId()+1
        self.c.execute("INSERT INTO sudoku VALUES(:id, :name) ",
                       {'id': id, 'name': sudoku_name})
        self.conn.commit()
        return id

    def add_blankSudokuLines(self, su_id: int):
        sql = "INSERT INTO sudokuLines VALUES(:sudokuId, :row, :col1, :col2, :col3, :col4, :col5, :col6, :col7, :col8, :col9) "

        for i in range(0, 9):
            self.c.execute(sql, {'sudokuId': su_id, 'row': i, 'col1': 0, 'col2': 0,
                           'col3': 0, 'col4': 0, 'col5': 0, 'col6': 0, 'col7': 0, 'col8': 0, 'col9': 0})
            self.conn.commit()

    def update_sudokuLine(self, sudokuId: int, row: int, col: int, value: int):
        column = "col"+str(col+1)
        sql = f"UPDATE sudokuLines SET {column} = :value WHERE sudokuId=:sudokuId AND row = :row"
        self.c.execute(sql, {'sudokuId': sudokuId, 'row': row, 'value': value})
        self.conn.commit()

    def insert_sudokuFromList(self, main_list: list, name):
        su_id = self.add_newSudoku(name)
        sql = "INSERT INTO sudokuLines VALUES(:sudokuId, :row, :col1, :col2, :col3, :col4, :col5, :col6, :col7, :col8, :col9) "
        for i in range(0, 9):
            self.c.execute(sql, {'sudokuId': su_id, 'row': i, 'col1': main_list[i][0], 'col2': main_list[i][1], 'col3': main_list[i][2], 'col4': main_list[
                           i][3], 'col5': main_list[i][4], 'col6': main_list[i][5], 'col7': main_list[i][6], 'col8': main_list[i][7], 'col9': main_list[i][8]})
            self.conn.commit()

    def get_AllSudoku(self):
        self.c.execute('SELECT * FROM sudoku')
        return self.c.fetchall()

    def get_sudokuFromLines(self, su_id: int):
        self.c.execute(
            'SELECT col1,col2,col3,col4,col5,col6,col7,col8,col9 FROM sudokuLines WHERE sudokuId=:sudokuId', {'sudokuId': su_id})
        return self.c.fetchall()
