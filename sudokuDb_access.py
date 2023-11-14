import sqlite3


class Sudoku_db:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('DBAccess/sudoku.db')
        self.c = self.conn.cursor()
        self.create_db()

    def create_db(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS sudoku (
                       id integer PRIMARY KEY,
                       name text,
                       data text
        ) """)
        self.conn.commit()

    def insert_data(self, name: str, data: str):
        self.c.execute("INSERT INTO sudoku (name,data) VALUES(:name ,:data)", {
                       'name': name, 'data': data})
        self.conn.commit()

    def view_allSudoku(self):
        self.c.execute('SELECT * FROM sudoku')
        return self.c.fetchall()

    def get_sudokuIdFromName(self, name: str):
        self.c.execute(
            "SELECT id FROM sudoku WHERE name =:name", {'name': name})
        data = self.c.fetchone()
        if data == None:
            data = ["No Data"]
        return data[0]

    def get_sudokuDataFromId(self, id):
        self.c.execute("SELECT data FROM sudoku WHERE id=:id", {'id': id})
        data = self.c.fetchone()
        if data == None:
            data = ["No Data"]
        return data[0]

    def transfer_sudokuToDataDb(self, sudoku_id, sudoku_name: str):
        sudoku_data = self.get_sudokuDataFromId(sudoku_id)

        from sqliteAccess import SqliteAccess
        my_sqlite = SqliteAccess()
        s_id = my_sqlite.add_newSudoku(sudoku_name)
        my_sqlite.add_blankSudokuLines(s_id)

        sudoku_dataList = sudoku_data.split(',')
        for i in sudoku_dataList:
            my_sqlite.update_sudokuLine(
                s_id, int(i[0])-1, int(i[1])-1, int(i[2]))

    def get_lastId(self):
        self.c.execute("SELECT id,name FROM sudoku ORDER BY id DESC LIMIT 1")
        data = self.c.fetchone()
        if data == None:
            data = ["No Data"]
        return data

    def close_db(self):
        self.conn.close()
