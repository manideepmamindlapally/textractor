import os
import shutil
import sys
from flask import Flask, render_template, request, url_for, redirect
from PIL import Image
from backend.get_text import textrecog

frontend = "./frontend/"
temp = "./temp/"
template_folder = frontend + "templates/"
app = Flask(__name__, template_folder = template_folder)

@app.route('/')
def main():
	return redirect(url_for("index"))

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/display')
def display():
	fimage_url = request.args['fimage_url']
	ftext = request.args['ftext']
	# shutil.rmtree('/home/me/test')
	return render_template("index.html", fimage_url= fimage_url, ftext=ftext)

@app.route('/', methods=["POST"])
def submit():
	image_url = request.form['imgurl']
	mode = request.form['mode']
	fimage, ftext = textrecog(image_url, mode)
	fimage.save(temp+"fimage.png")
	fimage_url = temp+"fimage.png"
	print(fimage_url)
	return redirect(url_for("display", fimage_url= fimage_url, ftext=ftext))

if __name__ == "__main__":
	app.run()