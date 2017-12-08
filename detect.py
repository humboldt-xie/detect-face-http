import tensorflow as tf
from scipy import misc
import numpy as np
import detect_face
import os
from os.path import join as pjoin

class Facedetect:
    minsize = 20  # minimum size of face
    threshold = [0.6, 0.7, 0.7]  # three steps's threshold
    factor = 0.709  # scale factor
    def __init__(self):
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.6)
        self.sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        self.pnet, self.rnet, self.onet = detect_face.create_mtcnn(self.sess, './align')
        self.minsize = 20  # minimum size of face
        self.threshold = [0.6, 0.7, 0.7]  # three steps's threshold
        self.factor = 0.709  # scale factor
   
    def detectStream(self,stream):
        img = misc.imread(stream, mode='RGB')
        img_size = np.asarray(img.shape)[0:2]
        bounding_boxes, _ = detect_face.detect_face(img, self.minsize, self.pnet, self.rnet, self.onet, self.threshold, self.factor)
        return bounding_boxes
    def detect(self,file):
        img = misc.imread(os.path.expanduser(file), mode='RGB')
        img_size = np.asarray(img.shape)[0:2]
        bounding_boxes, _ = detect_face.detect_face(img, self.minsize, self.pnet, self.rnet, self.onet, self.threshold, self.factor)
        return bounding_boxes
face=Facedetect()
print(face.detect("data/Anthony_Hopkins_0001.jpg"))
print(face.detectStream(open("data/Anthony_Hopkins_0002.jpg")))


