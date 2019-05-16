# Neuro Nexus 2019
This project is for the Neuro Nexus 2019 competition. Projects are invited from neuroscientists, clinicians, and mental health professionals. 120-150 participants, from a multitude of backgrounds, will then come together in teams of 5-7 individuals to work on the projects proposed over a period of 6 weeks. The program will culminate in a 72-hour hackathon weekend where access to prototyping resources are provided, and at Demo Night teams will showcase their projects to the community at large. 

Team Members:
* Helen Carlson
* James Peralta
* Brian Pho
* Amira Kalifa
* Aaron Leung
* Andy Wu

## Problem:
Our team Braining Edge, was tasked with creating a new algorithm to segment the human brain. Previous techniques used a set of probabilities chosen by the algorithm designer to guess which pixel belonged to a certain tissue type. Only problem with this approach is that there are many possible ways a tissue type appears on the MRI. This means means the algorithm designer must account for almost every single combination and as you can probably guess, previous techniques did not work too well.

## Solution:
We at Braining Edge have improved on these algorithms by using Deep Learning for this task. We trained a Convolutional Neural Network that took 23x23 patches surrounding a pixel to classify it as Grey Matter, White Matter, CSF, Dura or Skull. To classify a whole MRI scan it would iterate through every pixel and make a prediction on each pixel.

The training dataset was a variety of 23x23 patches from the MRIs found in the ATLAS dataset. 

## Technologies used
* Keras: High level Neural Network API
* Tensorflow: Backend Neural Network API
* Google Colab: Used for training the Neural Network
* Nilabel: Used for working with MRI scans
* Matplotlib, Skimage, CV2: Manipulating and displaying images
* Many other Python Libraries

## Challenges we ran into
* Working with MRI files was very interesting. The .nii images had pixel values of 0 to ~1400 which was causing some troubles when converting them to gray-scale. To fix this I just divided each MRI scan by it's max value to get the ranges between 0-1.
* The labels distribution was also a very big problem. When extracting patches to train the model on, most of the dataset were all black patches. I attempted to train with these black patches still in the dataset but my model was spitting out garbage. As soon as I removed 80% of the black patches my model began working again.
* It is also very important to always shuffle the training data. This helped increase my accuracy.
* Found this resource for debugging: https://blog.slavv.com/37-reasons-why-your-neural-network-is-not-working-4020854bd607
