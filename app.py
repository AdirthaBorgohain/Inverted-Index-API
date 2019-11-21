import os
from inverseindex import TapSearch
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/docidx', methods=['POST'])
def handle_document():
    doc = request.form['document']
    obj = TapSearch(doc)
    session["paragraphs"] = obj.get_paragraphs()
    session["inverted_index"] = obj.get_inverted_index()
    return render_template("word.html")

@app.route('/clear', methods=['POST'])
def clear_db():


@app.route('/search', methods=['POST'])
def search_term():
