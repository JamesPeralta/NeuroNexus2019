from sklearn.feature_extraction import image
from Common import show_images, retrieve_scan, show_slice
import numpy as np
import matplotlib.pyplot as plt


def retrieve_slice(slice_location):
    '''
    :param slice_location: Location of the slice
    :return: Slice as a numpy array
    '''
    scan = plt.imread(slice_location)

    # Pre-process the scan after reading it
    scan = norm_slice(scan)

    return scan


def norm_slice(slice):
    '''
    INPUT:  (1) a single slice of any given modality (excluding gt)
    OUTPUT: normalized slice
    '''
    b, t = np.percentile(slice, (0.5,99.5))
    slice = np.clip(slice, b, t)
    if np.std(slice) == 0:
        return slice
    else:
        return (slice - np.mean(slice)) / np.std(slice)