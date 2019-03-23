from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from PIL import Image
from backend.get_text import textrecog
from app import app

TEMP = app.config['TEMP']
MAXREQ = app.config['MAXREQ']
req = 0

@app.route('/')
def main():
	print(app['TEMP'])
	return redirect(url_for("index"))

@app.route('/index')
def index():
	return render_template("index.html")

# renders the final text display
@app.route('/display')
def display():
	fimage_name = request.args['fimage_name']
	ftext = request.args['ftext']
	return render_template("index.html", fimage_name= fimage_name, ftext=ftext)

# returns the image location src
@app.route('/display_im/<filename>')
def display_im(filename):
	return send_from_directory(TEMP, filename)

@app.route('/', methods=["POST"])
def submit():
	image_url = request.form['imgurl']
	mode = request.form['mode']
	fimage, ftext = textrecog(image_url, mode)
	
	global req
	req = (req+1)%MAXREQ
	# fimage_name = "fimage"+str(req)+".png"
	fimage_name = "fimage"+".png"
	fimage.save(TEMP+fimage_name)

	return redirect(url_for("display", fimage_name= fimage_name, ftext=ftext))