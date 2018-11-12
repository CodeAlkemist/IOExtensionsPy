import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ioutils",
    version="1.0.0.post1",
    author="Computer Raven",
    author_email="oss@compuraven.com",
    description="A package containing io utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeAlkemist/IOExtensionsPy/tree/master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)