from app import app
from flask import render_template

import decimal
import extractor

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html')

@app.route('/dev')
def dev_jobs():
	if extractor.text == "":
		content = {
		"text":"Nothing found",
		"url":" ",
		"realiblity":" ",
		}
	else:
		content = {
		"text": extractor.text,
		"url": extractor.link,
		"realiblity": round(decimal.Decimal(extractor.realiblity),2),
		}
		print extractor.link
	return render_template('dev_jobs.html', contents=content)

@app.route('/market')
def dev_market():
	content = {
	"text": extractor.text,
	"url": extractor.link,
	"realiblity": round(decimal.Decimal(extractor.realiblity),2),
	}
	print extractor.link
	return render_template('m_jobs.html', contents=content)


