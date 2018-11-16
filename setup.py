import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swan",
    version="1.0.0",
    author="Computer Raven",
    author_email="oss@compuraven.com",
    description="A package containing utilities to speed up development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeAlkemist/swan/tree/master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)