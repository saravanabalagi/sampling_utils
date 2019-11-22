from sampling_utils.sampling_functions import are_valid_samples
import pytest


valid_samples_list = [
    [0, 1],
    [1, 3],
    [3, 6, 4, 2, 8],
    [3, 6, 10, 15],
]
dont_pick_closest_list = [0, 1, 0, 1]


@pytest.mark.parametrize("valid_samples, dont_pick_closest", zip(valid_samples_list, dont_pick_closest_list))
def test_are_valid_samples(valid_samples, dont_pick_closest):
    assert are_valid_samples(valid_samples, dont_pick_closest)


