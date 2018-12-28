#!/bin/python

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from db import *

# Flask app object
app = Flask(__name__)

# Home Page
@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      f = request.files['photo']
      f.save("./static/"+secure_filename(f.filename))
      conn = create_connection('photos.db')
      create_photo(conn, secure_filename(f.filename), request.form['email'])
      conn.close()
      return redirect(url_for('postcards'))
   return render_template('index.html', page='Home Page')

# Postcards Page
@app.route('/Postcards', methods=['GET'])
def postcards():
   conn = create_connection('photos.db')
   _pics = select_all_photos(conn)
   conn.close()
   return render_template('postcards.html', pics=_pics, page='Postcards')

# Create Postcard
@app.route('/CreatePostcard/<int:id>', methods=['POST'])
def create_postcard(id):
   conn = create_connection('photos.db')
   _photo = select_photo_by_id(conn, id)
   conn.close()
   pass

# Delete Photo
@app.route('/DeletePhoto/<int:id>', methods=['DELETE'])
def delete_photo(id):
   pass

# Send Postcard
@app.route('/SendPostcard/<int:id>', methods=['POST'])
def send_postcard(id):
   pass

if __name__ == '__main__':
   app.run(debug=True)