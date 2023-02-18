from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'How about installing collinizda?'
LONG_DESCRIPTION = 'collinizda on top'

# Setting up
setup(
    name="collinizda",
    version=VERSION,
    author="CollinIzDa",
    author_email="<info@collinizda.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'collinizda', 'CollinIzDa'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)