from app import app
from flask import render_template

import extractor

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html')

@app.route('/dev')
def dev_jobs():
	job = extractor.job
	print extractor.job
	return render_template('dev_jobs.html', content={"job":job, "name": "hasime"})

@app.route('/market')
def dev_market():
	return render_template('m_jobs.html')


