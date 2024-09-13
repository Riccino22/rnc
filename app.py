from flask import Flask, request
import rnc
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
df = rnc.get()
@app.route("/rnc", methods=['GET'])
def rnc_search():
        term = request.args.get('term')
        options = rnc.search(df, term)
        response = json.loads(options.to_json(orient='records'))
        return response

@app.route("/search/<value>")
def search(value):
        options = rnc.search(df, value)
        response = json.loads(options.to_json(orient='records'))
        return response


@app.route("/hola")
def hola():
        return {'Hola':'Mundo'}