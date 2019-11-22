from sampling_utils.sampling_functions import get_min_samples, get_max_samples
import numpy as np
import pytest


population_list = [
    *[(np.arange(i)) for i in range(12)],
    [4, 5, 6, 8],
    [4, 5, 6, 10, 11],
    [4, 5, 6, 7, 8, 11, 13],
]
min_samples_list = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3,
                    1, 2, 2]
max_samples_list = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4,
                    2, 2, 3]
dont_pick_closest_list = [2 for _ in range(len(population_list))]


@pytest.mark.parametrize("population, dont_pick_closest, max_samples",
                         zip(population_list, dont_pick_closest_list, max_samples_list))
def test_get_max_samples(population, dont_pick_closest, max_samples):
    output = get_max_samples(population, dont_pick_closest)
    expected_output = max_samples
    assert (output == expected_output)


@pytest.mark.parametrize("population, dont_pick_closest, min_samples",
                         zip(population_list, dont_pick_closest_list, min_samples_list))
def test_get_min_samples(population, dont_pick_closest, min_samples):
    output = get_min_samples(population, dont_pick_closest)
    expected_output = min_samples
    assert (output == expected_output)
