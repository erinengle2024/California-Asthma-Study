from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.ext.automap import automap_base
import psycopg2

app = Flask(__name__)
# engine=create_engine('sqlite:///database.db', echo=True)
engine=create_engine('postgresql://postgres:postgres@localhost:5432/database.db')


# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
# Base.prepare(engine, reflect=True)
Base.prepare(engine)

# Base.prepare(engine, autoload_with=engine)


@app.route("/")
def home():
    # https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates
    return render_template('index.html')

@app.route('/data')
def get_data(): 
    query=text('''
               SELECT * 
               FROM survey_2018
               ''')
    conn=engine.connect()
    results=conn.execute(query)
    conn.close()
    results=[tuple(row[1:]) for row in results]
    return jsonify(results)
@app.route('/data2')
def get_data2(): 
    query=text('''
            SELECT * 
            FROM survey_2019
            ''')
    conn=engine.connect()
    results=conn.execute(query)
    conn.close()
    results=[tuple(row[1:]) for row in results]
    return jsonify(results)

@app.route('/data3')
def get_data3(): 
    query=text('''
            SELECT * 
            FROM survey_2022
            ''')
    conn=engine.connect()
    results=conn.execute(query)
    conn.close()
    results=[tuple(row[1:]) for row in results]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)