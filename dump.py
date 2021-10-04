from flask import Flask, json, request, jsonify, render_template, flash
import psycopg2
from markupsafe import escape

# Connect to your postgres DB
conn = psycopg2.connect("dbname=flask user=peterp")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM companies")

# Retrieve query results
records = cur.fetchall()

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(records)

@api.route('/companies', methods=['POST'])
def post_companies():
  pname = request.form["pname"]
  color = request.form["color"]
  entry = People(pname, color)
  db.session.add(entry)
  db.session.commit()
  return json.dumps({"success": True}), 201

# poster = cur.execute("""
# ...     INSERT INTO companies (name)
# ...     VALUES (%s);
# ...     """,
# ...     ("O'Reilly"))

if __name__ == '__main__':
    db.create_all()
    api.run(debug=True)