from app import app
from flask import render_template

import extractor

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html')

@app.route('/dev')
def dev_jobs(text ,url, realiblity):
	if text == "":
		content = {
		"text":"Nothing found",
		"url":" ",
		"realiblity":" ",
		}
	else:
		content = {
		"text":text,
		"url": url,
		"realiblity": realiblity,
		}
	print "it came here"
	return render_template('dev_jobs.html', content)

@app.route('/market')
def dev_market(*args, **kwargs):
	content = {
	"text": args.text,
	"url": args.url,
	"realiblity": args.realiblity,
	}
	return render_template('m_jobs.html', content)


