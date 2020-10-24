def timsort(arr, minrun):
    import ctypes, subprocess, os
    from array import array

    file_name = "timsort.py"
    path_to_sort = os.path.abspath(__file__)[:-len(file_name)] + "c_timsort/TimSort.so"
    c_lib = ctypes.cdll.LoadLibrary(path_to_sort)
    temp_arr = array('q', arr)
    addr, count = temp_arr.buffer_info();
    p = ctypes.cast(addr, ctypes.POINTER(ctypes.c_longlong))
    c_lib.PyList_Sort(p, ctypes.c_int(len(arr)), ctypes.c_int(minrun))

    return temp_arr.tolist()

