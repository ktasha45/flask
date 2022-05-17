from tensorflow.keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np

def load_model():
    model = ResNet50(weights="imagenet")
    return model

def prepare_image(image, target):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    return image

def solution(filename):
    image = Image.open(filename)
    image = prepare_image(image, target=(224, 224))
    model = load_model()
    pred = model.predict(image)
    result = imagenet_utils.decode_predictions(pred)
    return str(result[0][0][1]), str(result[0][0][2])