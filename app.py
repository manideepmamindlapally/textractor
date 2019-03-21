import os
import sys
from flask import Flask, render_template, request, url_for, redirect
from PIL import Image
from backend.get_text import textrecog

frontend = "./frontend/"
template_folder = frontend + "templates/"
app = Flask(__name__, template_folder = template_folder)

@app.route('/')
def main():
	return redirect(url_for("index"))

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/', methods=["POST"])
def submit():
	image_url = request.form['imgurl']
	mode = request.form['mode']
	print(mode)
	fimage, text = textrecog(image_url, mode)
	print(text)
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run()