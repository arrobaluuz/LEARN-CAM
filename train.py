import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator #preprocesar imagenes
from tensorflow.python.keras import optimizers #entrenar algoritmo
from tensorflow.python.keras.models import Sequential #permite hacer redes neuronales secuenciales (capas en orden)
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D #capas de convulsiones
from tensorflow.python.keras import backend as K

K.clear_session()
#Almacenar el directorio de imagenes
data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

#Parameteros de red neuronal
epocas=20 #numero de veces a iterar
longitud, altura = 100, 100 #tamaño a procesar imagenes (px)
batch_size = 26 #número de imagenes en cada paso
pasos = 10 #número de veces a procesar información
validation_steps = 10 #correr validación
filtrosConv1 = 32 #despues de conv1 tiene un profundidad de 32
filtrosConv2 = 64 #despues de conv2 tiene un profundidad de 64
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2)
clases = 4
lr = 0.0005

#preprocesamiento de imagenes
entrenamiento_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True)
validacion_datagen = ImageDataGenerator(rescale=1./255)

imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

imagen_validacion = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura,longitud),
    batch_size=batch_size,
    class_mode='categorical')

#crear la red CNN
cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding ="same", input_shape=(longitud, altura, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ="same",activation="relu"))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizers.adam_v2.Adam(lr=lr),
            metrics=['accuracy'])
cnn.fit_generator(
    imagen_entrenamiento,
    steps_per_epoch=pasos,
    epochs=epocas,
    validation_data=imagen_validacion,
    validation_steps=validation_steps)

dir = './modelo/'
if not os.path.exists(dir):
  os.mkdir(dir)
cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')