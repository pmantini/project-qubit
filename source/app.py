import os
import config
import logging
import utilities as webutils
from backend import PeriodicFilters
from backend import Filters
from backend.Operations import Operations
logging.basicConfig(level=config.logging_level, format='%(levelname)s - %(message)s')
import cv2
from flask import Flask
from flask import render_template, request, redirect, send_from_directory
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.DATA_PATH

current_image = ''


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']
    print(file, request.url)
    if file.filename == '':
        return redirect(request.url)

    if file and webutils.allowed_file(file.filename):
        filename = file.filename
        file.save(config.UPLOADED_IMAGE_FILE_PATH)
        return render_template('image.html', source=filename)


@app.route('/render/<filename>')
def send_image(filename):
    try:
        return send_from_directory('data/', filename)
    except FileNotFoundError:
        return send_from_directory('data/', 'not_available.png')

@app.route('/display', methods=['POST', 'GET'])
def change_display():
    if current_image == '':
        print("There's no current image loaded")
        return redirect(request.url)

    print("DISPLAY FLOW")
    print(current_image)
    print(request.json)

    if request.json['display'] != 'filtered':
        filename = '{}_{}'.format(request.json['display'], current_image)
    else:
        filename = current_image
    return render_template('image.html', source=filename)

@app.route('/apply', methods=['POST'])
def apply_filter():
    image_path = process_image(request.json)
    global current_image
    current_image = image_path
    print('>>> ', image_path)
    # print(request.json)
    #
    #
    #
    # image = cv2.imread(config.UPLOADED_IMAGE_FILE_PATH)
    # # params =
    # # params['filter_shape'] = image.shape
    #
    # if request.json['method'] == 'statistical':
    #     output_image = handle_statistical(params)
    # elif request.json['method'] == 'periodic':
    #     output_image = handle_periodic(params)
    # elif request.json['method'] == 'noise':
    #     output_image = handle_noise(params)
    # else:
    #     print("TRY AGAIN: NOT METHOD SPECIFY!")
    #     return redirect(request.url)

    return render_template('image.html', source = image_path)


# # TODO move these functions to the backend
# def handle_statistical(json):
#     print("handle statistical:", json)
#     return "Lenna.png"
#
# def handle_periodic(json):
#     print('>>>>', json)
#     func = json['settings']['bandreject_type']
#
#     # Filters.BR_IDEAL_FILTER()
#     PeriodicFilters.band_reject_ideal_filter(json['settings'])
#
#     print("handle periodic:", json)
#     return "Lenna.png"
#
# def handle_noise(json):
#     print("handle noise:", json)
#     return "Lenna.png"


def process_image(json_dict):
    op = Operations()

    # op.apply_filter({'filter_name': Filters.MEAN_ARITHMETIC_FILTER,
    #                  'filter_shape': (5, 4),
    #                  'high_pass': True
    #                  })

    return op.apply_filter(json_dict)


if __name__ == "__main__":
    app.run(port=8111, debug=True)
    # process_image()