from flask import Flask, json, request, jsonify, render_template, flash, redirect, url_for
import psycopg2

app = Flask(__name__)
db = "dbname=flask-toys user=peterp"



def connect():
  c = psycopg2.connect("dbname=flask-toys user=peterp")
  return c

def get_all_toys():
  conn = connect()
  cur = conn.cursor()
  cur.execute("SELECT * FROM toys")
  toys = cur.fetchall()
  cur.close()
  conn.close()
  return toys

def add_toy(name):
  conn = connect()
  cur = conn.cursor()
  cur.execute("INSERT INTO toys (name) VALUES (%s)", (name,))
  conn.commit()
  cur.close()
  conn.close()

@app.route('/toys', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    db.add_toy(request.form['name'])
    return redirect(url_for('index'))
  return render_template('index.html', toys=db.get_all_toys())