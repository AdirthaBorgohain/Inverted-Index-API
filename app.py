import os
from Tapsearch import TapSearch
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/handle_document', methods=['POST'])
def handle_document():
    doc = request.form['document']
#    print(doc)
    TS = TapSearch(doc)
    TS.create_inverse_index()
    session["inverted_index"] = TS.retrieve_dict()
    session["document_index"] = TS.retrieve_doc_dict()
    return render_template("function.html")

#@app.route('/clear', methods=['POST'])
#def clear_db():


@app.route('/search_term', methods=['POST'])
def search_term():
    term = request.form['term']
#    print(session["inverted_index"])
#    print(term)
    result = TapSearch.search_term(session["inverted_index"], session["document_index"], term)
    print('**********************')
#    print(result)
    return render_template("results.html", paragraphs = result)

if __name__ == "__main__":
    app.run()