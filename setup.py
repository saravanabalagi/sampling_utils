import pathlib
from setuptools import setup
from sampling_utils import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sampling_utils",
    version=__version__,
    description="Python tools to sample randomly with dont pick closest `n` elements constraints. "
                "Also contains a batch generator for the same to sample with replacement "
                "and with repeats if necessary.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/sampling_utils",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sampling_utils"],
    include_package_data=True,
    install_requires=['numpy'],
    tests_requires=['pytest']
)
