import setuptools

setuptools.setup(
    name="excel-injector",
    version="0.0.1",
    author="William Wyatt",
    author_email="wwyatt@ucsc.edu",
    description="Utility to search excel files and inject dictionaries into them.",
    long_description="Utility to search excel files and inject dictionaries into them.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Tsangares/market",
    include_package_data=True,
    install_requires=[
        'et-xmlfile>=1.0.1',
        'jdcal>=1.4.1',
        'numpy>=1.17.0',
        'openpyxl>=2.6.2',
        'pandas>=0.25.0',
        'python-dateutil>=2.8.0',
        'pytz>=2019.2',
        'six>=1.12.0',
        'xlrd>=1.2.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
