import tflite_runtime.interpreter as tflite
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image

interpreter = tflite.Interpreter(model_path="model_2024_hairstyle_v2.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]
target_size = input_details['shape']
target_size = target_size[1], target_size[2]

def donwload_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def predict(url):
    image = donwload_image(url)
    prepared_image = prepare_image(image, target_size)
    image_array = np.array(prepared_image, dtype=np.float32) / 255
    X = np.array([image_array])
    interpreter.set_tensor(input_details['index'], X)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details['index'])
    return float(output_data[0])


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return {"Prediction": result}