from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys

app = Flask(__name__)

@app.route('/') # URL에 웹페이지 연결하기
@app.route('/home')
def home():
    return render_template('hello.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/applyphoto')
def photo_apply():
    location = request.args.get('location')
    cleaness = request.args.get('clean')
    built_in = request.args.get('built')
    return render_template('apply_photo.html')

@app.route('/upload_done', methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save('static/img/' + secure_filename(uploaded_files.filename))

    return redirect(url_for('home'))

@app.route('/list')
def list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)