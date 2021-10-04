from flask import Flask, request, jsonify
from markupsafe import escape
import json
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("dbname=pets_hotel user=peterp")
cursor = conn.cursor()

@app.route('/api/test', methods=['GET'])
def index():
    if request.method == 'GET':
        print('/api/test GET route has been hit')
        return 'CONNECTED TO SERVER'

# Route for the Pets table
@app.route('/api/pets', methods=['GET', 'POST'])
def pets_route():
    # handle the GET request
    if request.method == 'GET':
        cursor.execute('SELECT * FROM "pets"')
        data = cursor.fetchall()
        print('data from pets GET:', data)
        return jsonify(data)

    elif request.method == 'POST':
        try:
            req = request.json
            data = [req['name'], req['breed'], req['color'], True, req['owner_id']]
            cursor.execute('INSERT INTO "pets" ("name", "breed", "color", "is_checked_in", "owner_id") VALUES(%s, %s, %s, %s, %s)', data)
            conn.commit()
            return "OK"
        except (Exception, psycopg2.Error) as error:
            req = request.json
            print(error)
            return 'ERROR!', 500, error

# Route for the Pets table with paramater for pet id
@app.route('/api/pets/<int:pet_id>', methods=['PUT', 'DELETE'])
def pet_byId_route(pet_id):
    try:
        if request.method == 'PUT':
            req = request.json
            if req['checkDirection'] == 'OUT':
                sql = 'UPDATE "pets" SET "is_checked_in" = false WHERE "id" = %s'
            elif req['checkDirection'] == 'IN':
                sql = 'UPDATE "pets" SET "is_checked_in" = true WHERE "id" = %s'
            else:
                return 'Something has gone wrong', 501
            
            cursor.execute(sql, [pet_id])
            conn.commit()
            return 'Request OK'

        elif (request.method == 'DELETE'):
            cur = conn.cursor()
            data = request.json
            queryText = """DELETE FROM "pets" WHERE id = %s; """
            cur.execute(queryText, [pet_id])
            conn.commit()
            return 'Was deleted by ID'
            
    except(Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)
        return error, 500

# Route for the Owners table
@app.route('/api/owners', methods=['POST'])
def owners_route():
    # handle the POST request
    if request.method == 'POST':
        try:
            req = request.get_json()
            SQL = 'INSERT INTO "owners" ("first_name", "last_name") VALUES (%s, %s);'
            data = [req['first_name'], req['last_name']]
            cursor.execute(SQL, data)
            conn.commit()
            print('in owners POST')
            return 'OK'
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database", error)
            return error, 500

if __name__ == '__main__':
    app.run(debug=True)