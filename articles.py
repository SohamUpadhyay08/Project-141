from crypt import methods
import json
from flask import Flask,jsonify,request
import csv

all_articles = []
liked_articles = []
disliked_articles = []

with open("articles.csv",encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/get_article")
def get_article():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success",
    })

@app.route("/liked_article",methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status" : "success"
    })

@app.route("/disliked_article",methods=["POST"])
def disliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status" : "success"
    })


app.run()