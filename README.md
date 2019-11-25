# Sampling Utils

![Pypi Version](https://img.shields.io/pypi/v/sampling_utils)
![Pypi Licence](https://img.shields.io/pypi/l/sampling_utils)
![Pypi Wheel](https://img.shields.io/pypi/wheel/sampling_utils)

Python tools to sample randomly with dont pick closest `n` elements constraints. 
Also contains a batch generator for the same to sample with replacement and with repeats if necessary.

## Installation

Simply install using `pip`

```sh
pip install sampling_utils
``` 

## Usage

### Dont Pick Closest

```python
from sampling_utils import sample_from_list
sample_from_list([1,2,3,4,5,6,7,8], dont_pick_closest=2)
```
You are guaranteed to get samples that are at least `dont_pick_closest` apart<sup>#</sup> (in value, not in indices). 
Here you will get samples where `sample` - `any_other_sample` is always greater than 2.

For example, if 2 is picked, no other item in range [2+`dont_pick_closest` and 2-`dont_pick_closest`] will be picked

Another example looped 5 times:
```python
for _ in range(5):
    sample_from_list([1,2,3,4,5,6,8,9,10,12,14], dont_pick_closest=2)

# Output
# [5, 10, 2, 14]
# [9, 6, 14, 1]
# [3, 8, 12]
# [10, 3, 6, 14]
# [2, 5, 8, 12]
```

If 12 is sampled, sampling 10 and 14 are not allowed since `dont_pick_closest` is 2. 
In other words, if `n` is sampled, then sampling anything from `[n-dont_pick_closest, ... n-1, n , n+1, ... n+dont_pick_closest]`
is not allowed (if present in the list).

<sup>#</sup>Will be called as **dont_pick_closest rule** hereafter. 


### Number of samples

You can also specify how many samples you want from the list using `number_of_samples` parameter. 
By default, you get maximum possible samples (without replacement).  

```python
for _ in range(5):
    sample_from_list([1,2,3,4,5,6,8,9,10,12,14], dont_pick_closest=2, num_samples=2)

# Output
# [8, 2]
# [6, 3]
# [12, 1]
# [4, 10]
# [9, 1]
```

If you try to sample more than what's possible, you will get an error saying that it's not possible.

### Min and max samples

You may want to just know how much you can sample from a given list obeying the **dont_pick_closest rule**

```python
from sampling_utils import get_min_samples, get_max_samples
print(get_min_samples([1,2,3,4,5,6,8,9,10,12,14], dont_pick_closest=2))
print(get_max_samples([1,2,3,4,5,6,8,9,10,12,14], dont_pick_closest=2))

# Output
# Min 3
# Max 4
```

### Sampling without replacement successively / Generating batches of samples for one epoch

If you want to successively sample without replacement i.e. sample as many samples from the list without repeating, 
you can use `batch_rand_generator` as shown below. 
This is particularly useful to generate batches of data 
until no more batches can be generated (equivalent to one epoch).  

```python
from sampling_utils import batch_rand_generator 
from sampling_utils import get_batch_generator_elements

batch_size = 2
brg = batch_rand_generator([1,2,3,4,5,6,8,9,10,12,14], batch_size=batch_size, dont_pick_closest=2)
print(get_batch_generator_elements(brg, batch_size=batch_size))
# Output
# [[1, 4], [8, 5], [14, 3], [2, 6]]
```
Notice that the elements  

- within each batch obey the **dont_pick_closest rule** _(e.g. 1 and 4 from batch 1)_
- from different batches need not obey the rule _(e.g. 4 and 5 from batch 1 and 2 respectively)._

## Contributing

Pull requests are very welcome.

1. Fork the repo
1. Create new branch with feature name as branch name
1. Check if things work with a jupyter notebook
1. Raise a pull request

## Licence

Please see attached [Licence](LICENCE)