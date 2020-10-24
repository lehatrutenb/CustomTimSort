def TimSort(arr, minrun=None):
    if minrun is None:
        minrun = 0

    import ctypes, subprocess, os
    from array import array

    c_lib = ctypes.CDLL(ctypes.CDLL(os.path.abspath("TimSort.so")))
    temp_arr = array('q', arr)
    addr, count = v.buffer_info();
    p = ctypes.cast(addr, ctypes.POINTER(ctypes.c_longlong))
    c_lib.PyList_Sort(p, ctypes.c_int(len(arr)), ctypes.c_int(2))

    return temp_arr.tolist()

