from flask import Flask, request, render_template, jsonify
from PIL import Image, ImageEnhance, ImageOps
import io
import numpy as np
import base64

app = Flask(__name__)

def pixel_to_braille(pixels):
    return chr(0x2800 + sum(2 ** i for i, p in enumerate(pixels) if p))

def convert_to_refined_dot_matrix(image, width=None, threshold=128, invert=False):
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    image = ImageOps.autocontrast(image, cutoff=2)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.5)
    img_gray = np.array(image.convert('L'))

    if invert:
        img_gray = 255 - img_gray

    aspect_ratio = image.height / image.width
    if width:
        width = int(width)
        height = int(width * aspect_ratio)
    else:
        width = image.width
        height = image.height

    img_resized = Image.fromarray(img_gray).resize((width, height), Image.LANCZOS)
    img_array = np.array(img_resized)

    result = []
    for y in range(0, height, 4):
        row = []
        for x in range(0, width, 2):
            block = img_array[y:y+4, x:x+2].flatten()
            dots = [p < threshold for p in block]
            char = pixel_to_braille(dots)
            row.append(char)
        result.append(''.join(row))

    ascii_art = '\n'.join(result)
    return ascii_art

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert_base64', methods=['POST'])
def convert_base64():
    data = request.json
    image_data = data['image'].split(',')[1]
    threshold = int(data['threshold'])
    invert = data['invert']
    width = data['width']
    width = int(width) if width else None

    img = Image.open(io.BytesIO(base64.b64decode(image_data)))
    ascii_art = convert_to_refined_dot_matrix(img, width=width, threshold=threshold, invert=invert)
    char_count = len(ascii_art)
    return jsonify({'ascii_art': ascii_art, 'char_count': char_count}), 200

if __name__ == '__main__':
    app.run(debug=True)