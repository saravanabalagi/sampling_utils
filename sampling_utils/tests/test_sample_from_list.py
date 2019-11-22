import numpy as np
import pytest

from sampling_utils import sample_from_list, are_valid_samples, get_min_samples, get_max_samples


population_list = []
dont_pick_closest_list = []

for i in range(20):
    for j in range(20):
        population_length = np.random.randint(1, 100)
        population_list.append(np.random.randint(0, 100, population_length))
        dont_pick_closest_list.append(j)


@pytest.mark.parametrize("population, dont_pick_closest", zip(population_list, dont_pick_closest_list))
def test_sample_from_list(population, dont_pick_closest):
    picked = sample_from_list(population, dont_pick_closest=dont_pick_closest)

    picked_len = len(picked)
    assert are_valid_samples(picked, dont_pick_closest)
    assert (get_min_samples(population,
                            dont_pick_closest) <= picked_len <= get_max_samples(population,
                                                                                dont_pick_closest))
    for element in picked:
        assert (element in population)
