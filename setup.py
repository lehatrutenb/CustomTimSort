import os
import sys
import platform
import distutils
from os import listdir
from sysconfig import get_paths
from os.path import isfile, join
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PATH = get_paths()["include"]


def create_file_with_includes():
    files = [file for file in listdir(PATH) if isfile(join(PATH, file))]
    with open("all_headers.h", 'w') as f:
        for file in files:
            if file not in ["pyexpat.h", "py_curses.h", "graminit.h"]:
                f.write(f"#include <{file}>" + "\n")

create_file_with_includes()

setuptools.setup(
    name='customtimsort',
    version='1.0.1',
    author='lehatr',
    author_email='lehatrutenb@gmail.com',
    description="Timsort sorting algorithm with custom minrun",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[('c', ['listobject.c']),
                ('h', ['listobject.h']), 
                ('c.h', ['clinic/listobject.c.h']),
               ],
    ext_modules=[
        setuptools.Extension("_ctimsort",
            sources=["timsort.c"],
            include_dirs=[
                os.path.join(os.getcwd(), ''),
                PATH,
            ],
            language='c',
        )
    ],
    py_modules=["get_minrun", "__utils_get_and_parse_data"],
    packages=["customtimsort"],
    install_requires=['numpy', 'tensorflow', 'keras']
)
