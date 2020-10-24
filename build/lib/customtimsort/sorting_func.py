def TimSort(arr, minrun=None):
    if minrun is None:
        minrun = 0

    import ctypes, subprocess, os
    from array import array

    c_lib = ctypes.cdll.LoadLibrary(os.path.abspath("TimSort.so"))
    temp_arr = array('q', arr)
    addr, count = temp_arr.buffer_info();
    p = ctypes.cast(addr, ctypes.POINTER(ctypes.c_longlong))
    c_lib.PyList_Sort(p, ctypes.c_int(len(arr)), ctypes.c_int(minrun))

    return temp_arr.tolist()

