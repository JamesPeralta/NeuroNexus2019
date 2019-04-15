"""
This is the Common library for all functions related to Brain scans i/o
"""

import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib


def retrieve_scan(location):
    """
    Retrieves the specified Brain Scan from storage

    :param location: Location of Brain scan along with file name
           Ex)  /Users/jamesperalta/Dev/Test.nii

    :return scan: Brain scan as a numpy array
    """
    scan = nib.load(location)
    scan = np.array(scan.dataobj)
    return scan


def show_slice(image):
    """
    Displays the image passed

    :param image: The image as a numpy array
    """
    plt.imshow(image)


# ----------------------------------------------------------------------
# Playing around with the functions
location = "/Users/jamesperalta/Desktop/NeuroNexus/HC/HC/HC_T1.nii"
scan = retrieve_scan(location)
print(scan[0].shape)

plt.imshow(scan[0])
