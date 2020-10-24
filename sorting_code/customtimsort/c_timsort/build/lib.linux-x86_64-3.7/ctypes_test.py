import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "PyList_Sort.so"
    c_lib = ctypes.CDLL(libname)
    arr = [1, 2, 3]
    print(c_lib.PyList_Sort((ctypes.c_int * len(arr))(*arr)))
