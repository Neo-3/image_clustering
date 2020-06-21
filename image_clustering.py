import os, shutil, glob, os.path
from PIL import Image as pil_image
import numpy as np
from sklearn.cluster import KMeans

targetdir = "./pipelineClusters"

def create_cluster(files, features, targetdir):
    number_clusters = 8
    kmeans = KMeans(n_clusters=number_clusters, random_state=0).fit(np.array(features))
    for i, m in enumerate(kmeans.labels_):
        print("Copy: %s / %s" %(i+1, len(kmeans.labels_)), end="\r")
        cluster_dir = targetdir + "/" + str(m) + "/"
        try:
            os.makedirs(cluster_dir)
        except OSError:
            pass
        shutil.copy(files[i], cluster_dir + str(i) + ".jpg")