from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
import database

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
    uploaded_files.save(f'static/img/{(database.now_index())+1}.jpeg')

    return redirect(url_for('home'))

@app.route('/list')
def list():
    house_list = database.load_list()
    length = len(house_list)
    return render_template('list.html', house_list = house_list, length = length)

@app.route('/house_info/<int:index>/')
def house_info(index):
    house_info = database.load_house(index)
    location = house_info["location"]
    cleaness = house_info["cleaness"]
    built_in = house_info["built_in"]

    photo = f"img/{index}.jpeg"

    return render_template("house_info.html", location = location, cleaness = cleaness, built_in = built_in, photo = photo)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)