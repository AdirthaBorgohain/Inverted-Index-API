import os
from Invsearch import InvSearch
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = os.urandom(69)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/handle_document', methods=['POST'])
def handle_document():
    doc = request.form['document']
    TS = InvSearch(doc)
    TS.create_inverse_index()
    session["inverted_index"] = TS.retrieve_dict()
    session["document_index"] = TS.retrieve_doc_dict()
    return render_template("function.html")

@app.route('/clear', methods=['GET'])
def clear_db():
    session["inverted_index"], session["document_index"] = InvSearch.clear_all(session["inverted_index"], session["document_index"])
    return render_template("index.html")

@app.route('/search_term', methods=['POST'])
def search_term():
    term = request.form['term']
    result = InvSearch.search_term(session["inverted_index"], session["document_index"], term)
    return render_template("results.html", documents = result, query = term)

if __name__ == "__main__":
    app.run()