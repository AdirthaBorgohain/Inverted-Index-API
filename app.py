import os
from Tapsearch import TapSearch
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/doc', methods=['POST'])
def handle_document():
    doc = request.form['document']
    TS = TapSearch(doc)
    TS.create_inverse_index()
    session["inverted_index"] = obj.retrieve_dict()
    session["document_index"] = retrieve_doc_dict()
    return render_template("word.html")

@app.route('/clear', methods=['POST'])
def clear_db():


@app.route('/search', methods=['POST'])
def search_term():
    term = request.form['term']
    result = TapSearch.search_term(session["inverted_index"], session["document_index"], term)
    return render_template("result.html", paragraphs = res)

if __name__ == "__main__":
    app.run()