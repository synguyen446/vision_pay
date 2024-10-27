import tensorflow as tf
import numpy as np

__model = None

def get_fruit(img_input):

    return __model.predict(img_input)


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __model
    if __model is None:
        __model = tf.keras.models.load_model("model/fruit_recognizer.keras")
        print(__model.summary())
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
