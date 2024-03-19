# ctypes_test.py
import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = str(pathlib.Path().absolute() / "clib_cal.so")
    print("path:", libname)

    c_lib = ctypes.CDLL(libname)

    c_lib.helloWorld()

    