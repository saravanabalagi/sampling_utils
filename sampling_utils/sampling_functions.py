import numpy as np
from typing import Union
from sampling_utils.helper_functions import _remove_diagonal


def get_max_samples(population: list, dont_pick_closest: int) -> int:
    # if there's nothing to choose
    if len(population) == 0:
        return 0

    max_count = 0
    temp = None

    # algorithm for finding max count
    for index, el in enumerate(population):
        if temp is None or temp + dont_pick_closest < el:
            max_count += 1
            temp = el
    return max_count


def get_min_samples(population: list, dont_pick_closest: int) -> int:
    # if there's nothing to choose
    if len(population) == 0:
        return 0

    min_count = 0
    temp = None

    # algorithm for finding max count
    for index, el in enumerate(population):
        if temp is None or temp + (2 * dont_pick_closest + 1) <= el:
            min_count += 1
            temp = el
    return min_count


def sample_from_list(population: Union[list, np.ndarray],
                     number_of_samples: int = None,
                     dont_pick_closest: int = 0) -> list:
    chosen = []
    remaining = population

    # validate if picking count from len(choices) is possible
    max_picks_possible = get_max_samples(population, dont_pick_closest)
    if number_of_samples is not None and number_of_samples > max_picks_possible:
        raise ValueError(f"It is impossible to pick {number_of_samples} elements from {len(population)} "
                         f"choices with don't pick closest {dont_pick_closest}.\n"
                         f"Choices: {population}\n"
                         f"Count required: {number_of_samples}\n"
                         f"Maximum samples possible: {max_picks_possible}")

    while True:

        # if there's nothing to choose from
        if len(remaining) == 0:

            # if count is specified, and validated
            # and if there's nothing to choose from
            # and if chosen is len than count
            # restart the whole process
            if number_of_samples is not None and len(chosen) < number_of_samples:
                chosen = []
                remaining = population
                continue

            # if there's no count specified
            # stop when there's no more, don't repeat
            break

        # don't choose already chosen
        choice = np.random.choice(remaining)
        chosen.append(choice)

        # remove choice and all elements closest choice for next pool to choose from
        choice_expanded = np.arange(choice - dont_pick_closest, choice + dont_pick_closest + 1)
        remaining = np.setdiff1d(remaining, choice_expanded)

        # while loop continue until we get count items sampled
        if number_of_samples is not None and len(chosen) == number_of_samples:
            break

    return chosen


def batch_rand_num_generator(choices: list, batch_size: int, dont_pick_closest: int, repeat_yield: int = 0):

    # sort the list first
    choices = sorted(choices)

    # generate 0 to labels as choice to pick from
    choices_with_replacement = choices
    served = 0

    # Keep running until conditions are met
    while True:

        # if we can't pick batch size from what's left, stop
        max_picks = get_max_samples(choices_with_replacement, dont_pick_closest)

        # if no batches are served before raise exception,
        # else simply stop yielding
        if batch_size > max_picks:
            if served == 0:
                raise ValueError(f"Choices: {len(choices_with_replacement)} | Don't pick closest: {dont_pick_closest}\n"
                                 f"Max Possible Picks: {max_picks} | Required: {batch_size}\n"
                                 f"Generator will not yield anymore. Stopping...\n")
            break

        # Choose for current batch and remove choices and their neighbours from next pool to select from
        chosen_for_batch = sample_from_list(choices_with_replacement,
                                            number_of_samples=batch_size,
                                            dont_pick_closest=dont_pick_closest)
        choices_with_replacement = np.setdiff1d(choices_with_replacement, chosen_for_batch)

        # Keep running until there's nothing more to choose
        if len(chosen_for_batch) == 0:
            break

        # Yield one by one
        served += 1
        for el in chosen_for_batch:
            if repeat_yield > 1:
                for _ in range(repeat_yield):
                    yield el
            else:
                yield el


def are_valid_samples(population: Union[list, np.ndarray], dont_pick_closest: int):
    if len(population) <= 1:
        return True

    population = np.array(population)
    distances = np.abs(population[None, :] - population[:, None])
    distances = _remove_diagonal(distances)
    min_distances = np.min(distances, axis=-1)
    valid_mask = min_distances > dont_pick_closest
    return all(valid_mask)
