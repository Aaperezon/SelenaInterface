import numpy as np
from keras_preprocessing import image
from keras.models import load_model

#cargar modelo
model = load_model('./cats&dog.h5')
prediction = ''
def Work(ifile):
    global prediction
    test_image = image.load_img(ifile, target_size = (64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    if result [0][0] == 1:
        prediction = 'C.lupus'
    else:
        prediction = 'Felis silvestris'
    return prediction
def GetPrediction():
    return prediction