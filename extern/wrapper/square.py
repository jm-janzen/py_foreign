
import ctypes
import os
import sys

class Math():

    #
    # Initialise here, so consumer does not need to instantiate
    #

    # Get path to compiled lib
    lib_path    = os.path.join("extern", "lib", "library.so")

    # Get handle to lib
    square_lib  = ctypes.cdll.LoadLibrary(lib_path)

    # Define C func prototype with int return
    prototype   = ctypes.CFUNCTYPE(ctypes.c_int)

    # Get handle on `square' func from lib
    square_func = prototype(("square", square_lib))

    @staticmethod
    def square(x) : return Math.square_func(int(x))


