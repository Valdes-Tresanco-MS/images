import setuptools
import versioneer
import warnings

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="images",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Mario",
    author_email="mario@out.com",
    description="Simple test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

import images
from pathlib import Path
warnings.warn(f'######################################################{Path(images.__file__).absolute()}')