from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
	return render_template('base.html')

@app.route('/dev')
def dev_jobs():
	return render_template('dev_jobs.html')

@app.route('/market')
def dev_market():
	return render_template('m_jobs.html')


