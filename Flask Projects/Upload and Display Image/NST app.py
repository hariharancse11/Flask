from flask import Flask,render_template,request, session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define upload folder
UPLOAD_FOLDER  = os.path.join('static','upload')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=("GET", "POST"))
def store_image():
    if request.method=='POST':


        img = request.files['upload-file']

        img_filename = secure_filename(img.filename)

        img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

        return render_template('index.html')

@app.route('/showimage')
def showimage():
    processed_img = session.get('uploaded_img_file_path', None)
    return render_template('result.html', show_image = processed_img)

if __name__ == "__main__":
    app.run(debug=True)