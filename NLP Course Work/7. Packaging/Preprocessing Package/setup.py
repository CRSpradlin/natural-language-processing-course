import setuptools

with open('README.md', 'r') as file:
    long_desc = file.read()

setuptools.setup(
    name = 'preprocess_crspradlin', # this should be unique
    version = '0.0.1',
    author = 'crspradlin',
    author_email = 'support@crspradlin.dev',
    description = 'This is an example package created as part of a Udemy course.',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    clissifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.5'
)