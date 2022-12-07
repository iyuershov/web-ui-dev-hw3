import base64
from io import BytesIO
from flask import Flask, render_template, request
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
        encoded_image = base64.b64encode(in_memory_image.getvalue())
        result_text = f'Class of your image: "{image_class[0][1]}"'
        prob_text = f'Probability: {str(image_class[0][2])[0:5]}'
        return render_template(
            'index.html', result_text=result_text, prob_text=prob_text, result_image=encoded_image.decode('utf-8')
        )

    return render_template('index.html')
