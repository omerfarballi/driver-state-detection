from keras.models import load_model

import pandas as pd

import tensorflow as tf

from keras.preprocessing.image import ImageDataGenerator
mod=load_model("C:/Users/omerf/Downloads/classification_model_VGG16.h5")

def model(img_path):
    def find_max_index(lst):
        lst=list(lst)
        max_val = max(lst) # listedeki en büyük değeri bulun
        max_index = lst.index(max_val) # en büyük değerin indexini bulun
        return max_index # indexi döndürün


    test_data=pd.DataFrame([[img_path,'asdasdasd']],columns=['path','label'])
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
    return find_max_index(pred[0])
