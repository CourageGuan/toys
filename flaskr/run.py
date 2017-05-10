# coding:utf-8
from flask import Flask,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5571208'
app.config['MYSQL_DB'] = 'user'
mysql.init_app(app)

@app.route('/post_data/<string:data>',methods=['GET','POST'])
def post_data(data):

    cur = mysql.connection.cursor()
    sql = "insert into data(data) values(%s)" % (data)
    cur.execute(sql)
    mysql.connection.commit()

    return data + ' OK'

@app.route('/get_data/',methods=['GET','POST'])
def get_data():

    cur = mysql.connection.cursor()
    sql = 'select * from data'
    cur.execute(sql)
    res = cur.fetchall()

    results = []
    data = {}

    for r in res:
        d = {}
        d['id'] = r[0]
        d['data'] = r[1]
        results.append(d)
    
    data['results'] = results

    return jsonify(data)

if __name__ == '__main__':

    #app.debug = True
    app.run(host='0.0.0.0')
