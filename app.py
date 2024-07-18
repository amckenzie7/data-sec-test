from flask import Flask, jsonify
from config import PII_DATA, FINANCIAL_DATA

app = Flask(__name__)

@app.route('/pii')
def get_pii():
    return jsonify(PII_DATA)

@app.route('/financial')
def get_financial():
    return jsonify(FINANCIAL_DATA)

if __name__ == '__main__':
    app.run(debug=True)
