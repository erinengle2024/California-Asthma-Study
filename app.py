from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text, inspect

app = Flask(__name__)
engine=create_engine('sqlite:///database.db', echo=True)
# engine=create_engine('postgresql://user:pass@localhost:5432/database.db')

@app.route("/")
def home():
    # https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates
    return render_template('index.html')

@app.route('/data')
def get_data(): 
    query=text('''
               SELECT * 
               FROM data_table
               ''')
    conn=engine.connect()
    results=conn.execute(query)
    conn.close()
    results=[tuple(row[1:]) for row in results]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)