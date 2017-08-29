from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Billy'} # fake user
	posts = [ # fake array of posts
		{
		
			'author': {'nickname': 'Konro'},
			'body': 'Beautiful day in Cameroon!'
		},
		{

			'author': {'nickname': 'Yolande'},
			'body': 'The Algorithm movie was so cool!'
		}
	]
	return 	render_template('index.html', title='Home', user=user, posts=posts)

