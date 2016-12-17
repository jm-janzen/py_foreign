## Python C Wrapper Example
It is my hope that this be used as a reference for others experimenting
with extending python with C[pp].  Comments, PRs welcome - I'm sure this
reference repo could be improved.

### Build Instructions
```bash
# After cloning this repo and cd-ing into it

make all
```

### Run Instructions
```bash
# After building

./calc_square.py <INT>
```

### Basic architecture
```bash
py_foreign
    ├── calc_square.py      # CLI to Python wrapper to C lib
    ├── extern
    │   ├── build
    │   │   └── square.o    # Makefile generated: shared obj
    │   ├── lib
    │   │   └── library.so  # Makefile generated: shared lib
    │   ├── src
    │   │   └── square.cpp  # C[pp] source code
    │   └── wrapper
    │       └── square.py   # Portal from calc_square and library
    ├── LICENSE             # MIT 4 lyfe
    ├── makefile            # Compiles C code and shared lib
    └── README.md           # This document
```
