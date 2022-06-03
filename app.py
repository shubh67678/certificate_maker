from PIL import Image, ImageFont, ImageDraw
from flask import Flask, send_file
import os
from flask import jsonify
app = Flask(__name__)


@app.route('/get_certificate/<name>', methods=('GET', 'POST'))
def get_image(name):
    """
    Return a random image from the ones in the static/ directory
    """
    image_path = f"static/{name}"
    print(image_path)
    return send_file(image_path, mimetype='image/png')


@app.route('/create_certificate/<name>', methods=('GET', 'POST'))
def create_certificate(name):
    make_certificate(name)
    image_path = f"static/{name}.png"
    print(image_path)
    return send_file(image_path, mimetype='image/png')


# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size


def make_certificate(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text.
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./static/" + name + ".png")
    print('Saving Certificate of:', name)

# if __name__ == "__main__":

#     names = ['Tushar Nankani', "Full Name", 'Some Long Ass Name Might Not Work']
#     for name in names:
#         make_certificates(name)

#     print(len(names), "certificates done.")
