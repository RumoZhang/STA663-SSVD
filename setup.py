import setuptools
import versioneer



setuptools.setup(
    name="STA663-SSVD",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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