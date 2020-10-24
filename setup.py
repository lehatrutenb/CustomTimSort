import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="customtimsort",
    version="0.0.43",
    author="lehatr",
    author_email="lehatrutenb@gmail.com",
    description="Timsort sorting algorithm with custom minrun",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lehatrutenb/FastTimSort",
    packages=['customtimsort'],
    package_dir={'customtimsort': 'sorting_code/customtimsort'},
    package_data={'customtimsort': ['c_timsort/*', 'c_timsort/clinic/*', 'c_timsort/cpython/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
