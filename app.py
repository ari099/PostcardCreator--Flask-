#!/bin/python

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from db import *
from PIL import Image, ImageDraw, ImageFont

# Flask app object
app = Flask(__name__)
message = "PostcardCreator"

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
   # Create Image object with the input image
   image = Image.open(_photo[1])

   # Initialize the drawing context with the image
   # object as background
   draw = ImageDraw.Draw(image)
   # Create font object with the font file and specify
   # desired size
   font = ImageFont.truetype('./fonts/lucon.ttf', size=10)

   # Starting position of the message
   (x, y) = (0, 0)
   color = 'rgb(255, 255, 255)' # Black color

   # Draw message
   draw.text((x, y), message, fill=color, font=font)

   # Save the edited image
   image.save(_photo[1])

   # Set Modified flag to 1
   modify_image(conn, _photo[0])

   # Close database connection
   conn.close()
   return redirect(url_for('postcards'))

# Delete Photo
@app.route('/DeletePhoto/<int:id>', methods=['POST'])
def delete_photo(id):
   conn = create_connection('photos.db')
   pic = select_photo_by_id(conn, id)
   # print(pic)
   delete_photo_by_id(conn, id)
   _pics = select_all_photos(conn)
   if os.path.exists("./static/" + pic[0][0]):
      os.remove("./static/" + pic[0][0])
   else: print("The file doesn't exist")
   conn.close()
   return redirect(url_for('postcards'))

# Send Postcard
@app.route('/SendPostcard/<int:id>', methods=['POST'])
def send_postcard(id):
   pass

if __name__ == '__main__':
   app.run(debug=True)