from flask import Flask, json
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

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(records)

@api.route('/companies', methods=['POST'])
def post_companies():
  return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run()