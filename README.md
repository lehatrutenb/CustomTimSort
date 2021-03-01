# CustomTimSort
CustomTimSort is a library where you can sort python objects using custom minruns.
How to use:
```
from customtimsort import timsort, get_minrun

minrun = get_minrun(len(yours_object))
timsort(yours_object, minrun)
```

## *get_minrun(array_size: int, path_to_data: string, model_name: string)* -> int
Returns predicted minrun for given object's size

:param array_size: size of array we want to predict minrun to
:param path_to_data: name of json file with keys mean, std, standard: "data.json"
:param model_name: name of model that will predict minrun, standard: "standard_model"


## *timsort(yours_object: some iterable obj, minrun: int)* -> int
Sorts yours_object using given minrun

:param yours_object: something that you want to sort (but you can't use timsort(yours_object=[...]))
:param minrun: timsort parameter for sorting (but you can't use timsort(minrun=[...]))
