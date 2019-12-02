import numpy as np
from typing import Generator, Union, Iterator, List


# Remove diagonal using strides
# https://stackoverflow.com/a/46736275/3125070
def _remove_diagonal(matrix_2d: np.ndarray) -> np.ndarray:
    m = matrix_2d.shape[0]
    strided = np.lib.stride_tricks.as_strided
    s0, s1 = matrix_2d.strides
    return strided(matrix_2d.ravel()[1:], shape=(m - 1, m), strides=(s0 + s1, s1)).reshape(m, -1)


def get_batch_generator_elements(generator: Union[Generator, Iterator],
                                 batch_size: int, num_batches: int = None,
                                 drop_remainder: bool = False) -> List[list]:
    batch_elements = []
    batch_elements_list = []
    for index, num in enumerate(generator):
        if index % batch_size is 0 and index is not 0:
            batch_elements_list.append(batch_elements)
            # do NOT use batch_elements.clear()
            # Create a new object and replace the reference
            batch_elements = []
            if num_batches is not None and len(batch_elements_list) >= num_batches:
                break
        batch_elements.append(num)
    if len(batch_elements) is not 0:
        if not drop_remainder or len(batch_elements) == batch_size:
            batch_elements_list.append(batch_elements)
    return batch_elements_list
