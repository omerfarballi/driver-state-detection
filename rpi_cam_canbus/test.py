from PIL import Image
import numpy  as np
# Fotoğrafı aç
import tensorflow as tf

base_model = tf.keras.models.load_model('model2.h5')

img = Image.open("C:/Users/omerf/Downloads/Compressed/train/test/img_34.jpg")

# Boyutunu yeniden boyutlandır
img_resized = img.resize((256, 256))

# NumPy dizisine dönüştür
img_array = np.array(img_resized)

# İsteğe bağlı olarak, boyutları biraz değiştirebilirsiniz
img_array = np.expand_dims(img_array, axis=0)

im_reshaped = img_array.reshape((1, 256, 256, 3))
print(im_reshaped.shape)
ypred = base_model.predict(im_reshaped/255)
print(ypred)
ypred_class = np.argmax(ypred,axis=1)
print(ypred_class)
