from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = { 'username': 'Sam' }

	posts = [
		{
			'author': {'username': 'Sam'} ,
			'body': 'Hello world, My first post!'
		},
		{
			'author': {'username': 'Sam'},
			'body': 'My second post! Ola!'
		}
	]

	return render_template('index.html',title='Home',user=user, posts=posts)
