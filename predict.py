from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import numpy as np
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from numpy import interp
from sklearn.metrics import roc_auc_score
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import os, random, shutil, os.path, shutil, pandas, glob
from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
import numpy as np
import numpy
from keras.preprocessing import image
from tensorflow.keras import layers
from PIL import Image
import glob #file list
import pandas #read csv
import os #split file name
import shutil

images = glob.glob("predict/*.png")
images = sorted(images)

model = load_model('tridactyl_tracks_nn_v1.h5', compile = True)

#create empty array
tracks = [0]*len(images)
predictions = [0]*len(images)

for i in range(len(images)):
        image = tf.keras.utils.load_img(images[i],color_mode='grayscale')
        image = tf.keras.utils.img_to_array(image)
        image = np.expand_dims(image, axis = 0)/255
        prediction = model.predict(image)
        tracks[i] = prediction

results = tracks

for i in range(len(results)):
         arraytoocomplex = np.concatenate([[results[i]],[results[i]]])
         simplifiedarray = arraytoocomplex[:,:,0]
         simplifiedarray = simplifiedarray[:,0]
         results[i] = simplifiedarray

import pandas as pd
#tidy file name list
for i in range(len(images)):
        images[i] = images[i].replace('predict/','')
        images[i] = images[i].replace('.png','')

column_names = ['nn_model','nn_model2']
results = pd.DataFrame(results)
results.index = images #row names
results.columns = column_names
pd.DataFrame(results["nn_model"]).to_csv("predictions.csv")
print(results["nn_model"])
print("Estimates exported to file predictions.csv")
