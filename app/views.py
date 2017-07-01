from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
	return render_template('base.html')

@app.route('/jobs')
def assigned_jobs():
	return render_template('jobs.html')
