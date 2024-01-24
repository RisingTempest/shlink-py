from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Library to extract information from Shlink'
LONG_DESCRIPTION = 'This library has been created to facilitate the extraction of information from Shlink in a simple manner. It also allows for the seamless addition of new functions to extract different types of information. Feel free to add or delete words to enhance the description.'

setup(
       
        name="py-link", 
        version=VERSION,
        author="Jason Dsouza",
        author_email="<tuemail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
        'requests==2.31.0',
        'typing_extensions==4.8.0',
        ],
        
        keywords=['python', 'shlink'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "License :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
        ]
)