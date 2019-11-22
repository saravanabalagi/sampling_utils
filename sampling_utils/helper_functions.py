import numpy as np


# Remove diagonal using strides
# https://stackoverflow.com/a/46736275/3125070
def _remove_diagonal(matrix_2d):
    m = matrix_2d.shape[0]
    strided = np.lib.stride_tricks.as_strided
    s0,s1 = matrix_2d.strides
    return strided(matrix_2d.ravel()[1:], shape=(m-1, m), strides=(s0+s1, s1)).reshape(m, -1)