from setuptools import setup, find_packages
from os import path

setup(
      name="STA663-SSVD",
      version=1.0,
      description="SSVD Biclustering Algorithm",
      url='https://github.com/RumoZhang/STA663-SSVD',
      author="Rumo Zhang, Xige Huang",
      author_email="xh90@duke.edu",
      classifiers=[
                  'Development Status :: 3 - Alpha',
                  'Intended Audience :: Developers',
                  'Topic :: Software Development :: Libraries :: Python Modules',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.4',
                  'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                  ],
      packages=find_packages(),
      python_requires='>=3',
      )