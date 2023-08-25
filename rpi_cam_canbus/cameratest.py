from keras.models import load_model

import pandas as pd

import tensorflow as tf
mod=tf.keras.models.load_model("C:/Users/omerf/Downloads/classification_model_VGG16.h5")


def find_max_index(lst):
    lst=list(lst)
    max_val = max(lst) # listedeki en büyük değeri bulun
    max_index = lst.index(max_val) # en büyük değerin indexini bulun
    return max_index # indexi döndürün


test_data=pd.DataFrame([[f'C:/Users/omerf/Downloads/Compressed/train/test/img_34.jpg','asdasdasd']],columns=['path','label'])
Fseries = pd.Series(test_data.path, name="filepaths")
Lseries = pd.Series(test_data.label, name="labels")
data = pd.concat([Fseries,Lseries], axis=1)
df = pd.DataFrame(data)
image_gen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function= tf.keras.applications.mobilenet_v2.preprocess_input)
test = image_gen.flow_from_dataframe(dataframe= df,x_col="filepaths", y_col="labels",
                                    class_mode='categorical',batch_size=2,shuffle= False)
print(test.image_shape)
print(type(test))
mod.evaluate(test, verbose=1)

pred = mod.predict(test)
print(pred[0])
print(find_max_index(pred[0]))



import pandas as pd
import cv2
import numpy as np
import time
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
def find_max_index(lst):
    lst=list(lst)
    max_val = max(lst) # listedeki en büyük değeri bulun
    max_index = lst.index(max_val) # en büyük değerin indexini bulun
    return max_index # indexi döndürün


test_data=pd.DataFrame([[f'C:/Users/omerf/Downloads/Compressed/train/test/img_34.jpg','None']],columns=['path','label'])
Fseries = pd.Series(test_data.path, name="filepaths")
Lseries = pd.Series(test_data.label, name="labels")
data = pd.concat([Fseries,Lseries], axis=1)
df = pd.DataFrame(data)
image_gen = ImageDataGenerator(preprocessing_function= tf.keras.applications.mobilenet_v2.preprocess_input)
test = image_gen.flow_from_dataframe(dataframe= df,x_col="filepaths", y_col="labels",
                                    class_mode='categorical',batch_size=6,shuffle= False)
mod.evaluate(test, verbose=1)
pred = mod.predict(test)
print(pred[0])
print(find_max_index(pred[0]))