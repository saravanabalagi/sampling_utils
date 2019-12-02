from sampling_utils.sampling_functions import batch_rand_generator, are_valid_samples
import numpy as np
import pytest


population_list = []
batch_size_list = []
dont_pick_closest_list = []

for i in range(20):
    for j in range(1, 5):
        for k in range(5):
            population_length = np.random.randint(50, 200)
            population_list.append(np.random.randint(0, 100, population_length))
            batch_size_list.append(j)
            dont_pick_closest_list.append(k)


@pytest.mark.parametrize("population, batch_size, dont_pick_closest",
                         zip(population_list, batch_size_list, dont_pick_closest_list))
def test_batch_rand_generator(population, batch_size, dont_pick_closest):
    gen = batch_rand_generator(population, batch_size, dont_pick_closest)
    samples = np.array([sample for sample in gen])
    samples_batch = samples.reshape(-1, batch_size)

    # check if all samples belong to population
    for sample in samples:
        assert (sample in population)

    # check if no two batches can have common samples
    assert (len(set(samples)) == len(samples))

    # check if each batch is valid
    for batch in samples_batch:
        assert are_valid_samples(batch, dont_pick_closest)


population_list = []
batch_size_list = []
dont_pick_closest_list = []
expected_samples_list = []

for i in range(20, 50):
    for j in range(1, 5):
        known_population = np.arange(i)
        np.random.shuffle(known_population)
        population_list.append(known_population)
        batch_size_list.append(j)
        dont_pick_closest_list.append(0)
        expected_samples_list.append(i - (i % j))


@pytest.mark.parametrize("population, batch_size, dont_pick_closest, expected_samples",
                         zip(population_list, batch_size_list, dont_pick_closest_list, expected_samples_list))
def test_batch_rand_generator_misses_elements(population, batch_size, dont_pick_closest, expected_samples):
    test_batch_rand_generator(population, batch_size, dont_pick_closest)
    gen = batch_rand_generator(population, batch_size, dont_pick_closest)
    gen_len = sum(1 for _ in gen)
    assert gen_len == expected_samples
