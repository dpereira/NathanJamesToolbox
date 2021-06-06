import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='NathanJamesToolbox',
    version='1.3.15',
    description='Collection of tools developed for NathanJames',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pfajardo-nj/NathanJamesToolbox',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    packages=['NathanJamesToolbox'],
    include_package_data=True,
    install_requires=[
        'requests==2.25.1',
        'slacker==0.14.0',
        'datetime',
        'google-cloud-storage==1.32.0',
        'pymysql',
        'selenium'
    ]
)
