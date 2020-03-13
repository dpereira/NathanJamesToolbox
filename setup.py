import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='NathanJamesToolbox',
    packages=setuptools.find_packages(),
    version='0.1',
    description="Package for NJ scripts",
    scripts=['NathanJamesToolbox'],
    author="Paulo Fajardo",
    author_email="paulo.fajardo@nathanjames.com",
    download_url='https://github.com/pfajardo-nj/NathanJamesToolbox',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
