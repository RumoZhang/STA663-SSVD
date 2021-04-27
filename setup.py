from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('SSVD/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name="STA663-SSVD",
    version=main_ns['__version__'],
    url='https://github.com/RumoZhang/STA663-SSVD',
    author="Rumo Zhang, Xige Huang",
    author_email="xh90@duke.edu",
    description="SSVD Biclustering Algorithm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3'
)