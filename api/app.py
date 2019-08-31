from flask import Flask, request, jsonify, render_template
import sqlite3 as sqlite
import sys
import os
app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
@app.route('/', methods=['GET'])
def home():
    return """<h1>Stocks API</h1>
    <p>API for retrieving stock information</p>
    """

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/api/v1/resources/stocks/all', methods=['GET'])
def api_all():
    conn = sqlite.connect('../data/stocks.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_stocks = cur.execute("SELECT * FROM Stocks;").fetchall()
    return jsonify(all_stocks)

@app.route("/api/v1/resources/stocks", methods=['GET'])
def api_filter():
    query_parameters = request.args
    
    ticker = query_parameters.get('ticker')
    if not ticker:
        return page_not_found(404)

    to_filter = []
    query = build_select_stocks_query(ticker, to_filter)
    conn = sqlite.connect('../data/stocks.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)



def build_select_stocks_query(ticker, to_filter):
    query = "SELECT * FROM Stocks WHERE"
    if ticker:
        query += ' ticker=? AND'
        to_filter.append(ticker)

    query = query[:-4] + ';' # trims off _AND
    return query


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

