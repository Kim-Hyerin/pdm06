import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

from keras.datasets import cifar10

# Load CIFAR-10 dataset using tensorflow.keras
# Dividing data into training and test set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
class_names = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

# Sidebar
st.sidebar.header('CIFAR-10')
st.sidebar.subheader('DATA')
# Show a random image
if st.sidebar.checkbox('Show a random training image from CIFAR10'):
    numtr = np.random.randint(0, x_train.shape[0])
    image = x_train[numtr]
    st.sidebar.image(image, caption=class_names[y_train[numtr].item()], width=192)

if st.sidebar.checkbox('Show a random test image from CIFAR10'):
    numte = np.random.randint(0, x_test.shape[0])
    image = x_test[numte]
    st.sidebar.image(image, caption=class_names[y_test[numte].item()], width=192)

# Main 
st.title('DL using CNN2D_pdm06')
st.header('Dataset: cifar10')
#spending a few lines to describe our dataset
st.text("""Dataset of 50,000 32x32, 3 (rgb) training images, 
        labeled over 0 to 9, 
        and 10,000 test images.""")

# Information of cifar10 dataset
# (x_train, y_train), (x_test, y_test) = cifar10.load_data()
if st.checkbox('Show images sizes'):
    st.write(f'##### X Train Shape: {x_train.shape}') 
    st.write(f'##### X Test Shape: {x_test.shape}')
    st.write(f'##### Y Train Shape: {y_train.shape}')
    st.write(f'##### Y Test Shape: {y_test.shape}')

st.write('***')

if st.checkbox('Show 10 different image from the train set'):
    num_10 = np.unique(y_train, return_index=True)[1]
#     st.write(num_10)
    imagestr = x_train[num_10]
    for i in range(len(imagestr)):
        # define subplot
        plt.subplot(2,5,1 + i) #, sharey=False)
        # plot raw pixel data
        plt.imshow(imagestr[i])
        plt.title(class_names[i])
        plt.xticks([])
        plt.yticks([])
    plt.suptitle("10 different images", fontsize=16)
    st.pyplot()  # Warning

if st.checkbox('Show 10 different image from the test set'):
    num_11 = np.unique(y_train, return_index=True)[1]
#     st.write(num_11)
    imageste = x_test[num_11]
    for i in range(len(imageste)):
        # define subplot
        plt.subplot(2,5,1 + i) #, sharey=False)
        # plot raw pixel data
        plt.imshow(imageste[i])
        plt.title(class_names[i])
        plt.xticks([])
        plt.yticks([])
    plt.suptitle("10 different images", fontsize=16)
    st.pyplot()  # Warning