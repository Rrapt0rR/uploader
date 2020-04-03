import os, random
import json
import requests
import datetime
from random import choice
from jinja2 import Template
from datetime import timedelta
from dateutil.relativedelta import *
from flask import render_template, flash, redirect, session, url_for, request, flash, jsonify, json, make_response
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .models import User
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './app/static/files/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'zip', 'rar', 'pdf', 'tgz', '7z'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

path = os.getcwd()+"/app/static/files"
list_of_files = {}

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('uploader.html'), 404

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/index', methods=['GET', 'POST'])
#def index():
#	return redirect('uploader')

@app.route('/')
@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    #size = os.path.getsize(file)
    #size = [file for file in size if not file.startswith(".")]
    hists = os.listdir(os.path.join(app.static_folder, 'files'))
    hists = [file for file in hists if not file.startswith(".")]
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file'] 
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            code = ''.join(random.choice('123456789ABCDEFGHIJKLMNPQRSTUVWXYZ') for i in range(3))
            filename = secure_filename(code+'-'+file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #flash('File Uploaded Seccuessfuly')
            res = make_response(jsonify({"message": "File uploaded"}), 200)
            return res
    return render_template('uploader.html', hists=hists)