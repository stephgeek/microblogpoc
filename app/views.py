from app import app

@app.route('/')
@app.route('/index')
@app.route('/hello')
def index():
	return "Hello World!"

