import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import glob
import random
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category = FutureWarning)


os.chdir('Visao/Tarefa_3/BallDataset/')
if os.path.isdir('train/') is False:
    os.mkdir('train/')
    os.mkdir('valid/')
    os.mkdir('test/')
    os.mkdir('train/ball/')
    os.mkdir('train/no_ball/')
    os.mkdir('valid/ball/')
    os.mkdir('valid/no_ball/')
    os.mkdir('test/ball/')
    os.mkdir('test/no_ball/')

    os.chdir('ball/')
    for c in random.sample(glob.glob('*'),200):
        shutil.move(c,'train/ball/')
    for c in random.sample(glob.glob('*'),20):
        shutil.move(c,'valid/ball/')
    for c in random.sample(glob.glob('*'),30):
        shutil.move(c,'test/ball/')

    os.chdir('no_ball/')
    for c in random.sample(glob.glob('*'),75):
        shutil.move(c,'train/no_ball/')
    for c in random.sample(glob.glob('*'),5):
        shutil.move(c,'valid/no_ball/')
    for c in random.sample(glob.glob('*'),20):
        shutil.move(c,'test/no_ball/')

os.chdir('../../')

train_path = '/media/paulo/Novo volume/Curso python/Trainee_EDROM/Visao/Tarefa_3/BallDataset/train'
valid_path = '/media/paulo/Novo volume/Curso python/Trainee_EDROM/Visao/Tarefa_3/BallDataset/valid'
test_path = '/media/paulo/Novo volume/Curso python/Trainee_EDROM/Visao/Tarefa_3/BallDataset/test'


train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=train_path, classes = ['ball', 'no_ball'] ,target_size=(224,224),batch_size=10)
valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=valid_path,classes = ['ball', 'no_ball'], target_size=(224,224),batch_size=10)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=test_path,classes = ['ball', 'no_ball'], target_size=(224,224),batch_size=10, shuffle=False)

assert train_batches.n == 275
assert valid_batches.n == 25
assert test_batches.n == 50
assert train_batches.num_classes == valid_batches.num_classes == test_batches.num_classes == 2

model = Sequential([
        Conv2D(filters=32,kernel_size=(3,3),activation='relu',padding = 'same',input_shape=(224,224,3)),
        MaxPool2D(pool_size=(2,2),strides=2),
        Conv2D(filters=64,kernel_size=(3,3),activation='relu',padding = 'same'),
        MaxPool2D(pool_size=(2,2),strides=2),
        Flatten(),
        Dense(units = 2, activation='softmax'),
])



model.compile(optimizer= Adam(learning_rate=0.0001),loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x=train_batches,validation_data=valid_batches,epochs=3,verbose=2)


predictions = model.predict(x=test_batches,verbose=0)

cm=confusion_matrix(y_true=test_batches.classes,y_pred=np.argmax(predictions,axis=-1))

def plot_confusion_matrix(cm,classes,normalize=False,title='Confusion Matrix',cmap=plt.cm.Blues):
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks=np.arange(len(classes))
    plt.xticks(tick_marks,classes,rotation=45)
    plt.yticks(tick_marks,classes)

    if normalize:
        cm=cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")
    
    print(cm)

    tresh = cm.max()/2

    for i, j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,cm[i,j],
                horizontalalignment="center",
                color="white" if cm[i,j]>tresh else "Black")
    
    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")


cm_plot_labels = ['ball', 'no ball']
plot_confusion_matrix(cm=cm,classes=cm_plot_labels,title="Confusion matrix")
