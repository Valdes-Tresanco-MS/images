import setuptools
import versioneer
import warnings

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_images_pypi",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Mario",
    author_email="mario@out.com",
    description="Simple test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
