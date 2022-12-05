from io import BytesIO
from flask import Flask, render_template, request, flash
from model import classify_image

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.files.get('image') is not None:
        image = request.files.get('image')
        in_memory_image = BytesIO()
        image.save(in_memory_image)
        image_class = classify_image(in_memory_image)
        return render_template('index.html', result=image_class)
    else:
        flash('upload error')
    return render_template('index.html', result='')
