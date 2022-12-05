import numpy as np

from io import BytesIO
from keras.preprocessing.image import image_utils
from keras.applications.resnet import ResNet50
from keras.applications.resnet import preprocess_input
from keras.applications.imagenet_utils import decode_predictions

resnet = ResNet50(weights='imagenet')


def classify_image(img: BytesIO):
    img = image_utils.load_img(img, target_size=(224, 224))
    img = image_utils.img_to_array(img)
    x = preprocess_input(np.expand_dims(img.copy(), axis=0))
    predictions = resnet.predict(x)
    return decode_predictions(predictions, top=1)
