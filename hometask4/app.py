
import os
from flask import Flask, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from hometask3.images import *

UPLOAD_FOLDER = 'd:/images_for_converting/'
CONVERTED_IMAGES_FOLDER = "d:/images_black/"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_IMAGES_FOLDER'] = CONVERTED_IMAGES_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            clear_folder(CONVERTED_IMAGES_FOLDER)
            list_of_images = read_image_files(UPLOAD_FOLDER)
            convert_images(list_of_images, CONVERTED_IMAGES_FOLDER)
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return send_from_directory(app.config['CONVERTED_IMAGES_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)