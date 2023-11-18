from flask import Flask, request, jsonify
from flask_cors import CORS
from DBAccess.sqliteAccess import SqliteAccess
from sudokuDb_access import Sudoku_db
import functions
import json

app = Flask(__name__)
# app.config["DEBUG"] = True
CORS(app)


@app.route("/get-Sudoku")
def get_user():
    db = SqliteAccess()
    user_data = db.get_AllSudoku()

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200


@app.route("/get-Sudoku/<su_id>")
def get_sudokuData(su_id):
    db = SqliteAccess()
    user_data = db.get_sudokuFromLines(su_id)

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201


@app.route("/create-Sudoku", methods=["POST"])
def create_sudoku():
    data = request.get_json()
    sudoku_name = data["sudoku_name"]
    sudoku_data = data["sudoku_data"]
    db = Sudoku_db()
    db.insert_data(sudoku_name, sudoku_data)
    sudokuId = db.get_sudokuIdFromName(sudoku_name)
    db.transfer_sudokuToDataDb(sudokuId, sudoku_name)

    db = SqliteAccess()
    user_data = db.get_AllSudoku()
    sudokuId = db.get_latestSudokuId()

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify({'sudokuList': user_data, 'sudokuId': sudokuId, 'sudokuName': sudoku_name}), 200


@app.route("/solve-Sudoku", methods=["POST"])
def solve_sudoku():
    data = request.get_json()
    # sudoku_data = json.loads(data)
    # gridData = functions.create_blankGrid()
    # sudoku_dataList = sudoku_data.split(',')
    # for i in sudoku_dataList:
    #    gridData[int(i[0])-1][int(i[1])-1] = int(i[2])
    _result = functions.solve_sudoku(data)

    return jsonify(_result['main_grid']), 200


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
