import ctypes
import pathlib
import subprocess
import os

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = "TimSort.so"
    c_lib = ctypes.CDLL(os.path.abspath("TimSort.so"))
    from array import array
    v = array('q',[4,2,1,4,5])
    addr, count = v.buffer_info();
    p = ctypes.cast(addr,ctypes.POINTER(ctypes.c_longlong))
    c_lib.PyList_Sort(p, ctypes.c_int(5), ctypes.c_int(2))
    print(v.tolist())

