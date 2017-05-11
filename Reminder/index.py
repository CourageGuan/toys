#-*- coding: utf-8 -*-
import re
import sqlite3

from flask import Flask, flash, g, redirect, render_template, request, url_for

app = Flask(__name__)

app.config['DATABASE'] = './test.db'
app.secret_key = 'reminder'

def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	if not hasattr(g,'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

def close_db():
	if hasattr(g,'sqlite_db'):
		g.sqlite_db.close() 

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.route('/' ,methods=['POST','GET'])
def index():
	error = None
	url = ''
	keyword = ''
	mail = ''
	if request.method == 'POST':
		url = request.form['url']
	 	keyword = request.form['keyword']
	 	mail = request.form['mail']
		if not re.match(r'(https?)://[-A-Za-z0-9.]+\.[A-Za-z]+[/A-Za-z0-9.+-~#@%=_]+$', url):
			error = 'Wrong Url'
		elif not re.match(ur'[\u4e00-\u9fa50-9A-Za-z\_]+$', keyword):
			error = 'Wrong Keyword'
		elif not re.match(r'[A-Za-z0-9-]+@[A-Za-z0-9-.]+\.[A-Za-z]+$', mail):
			error = 'Wrong E-Mail'
		else:
			flash('A message will send to your e-mail when the url has the keyword.')
			get_db().execute('insert into info (url,keyword,mail) values(?,?,?)',[url,keyword,mail])
			get_db().commit()

			return redirect(url_for('index'))
			
	return render_template('index.html',error=error, url=url, keyword=keyword, mail=mail)

if __name__ == '__main__':
	#init_db() 
	app.run('0.0.0.0')
	close_db()
