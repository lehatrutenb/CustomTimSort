# CustomTimSort
CustomTimSort is a library where you can sort python objects using custom minruns.
How to use:
```
from timsort import timsort, get_minrun

minrun = get_minrun(len(yours_object))
timsort(yours_object, minrun)
```

## *get_minrun(len_of_yours_object: int)* -> int
Returns predicted minrun for given object's size

## *timsort(yours_object: some iterible obj, minrun: int)* -> int
Sorts yours_object using given minrun

