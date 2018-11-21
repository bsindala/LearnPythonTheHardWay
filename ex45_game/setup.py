try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = [
    'description' : 'Game Of Countries',
    'author' : 'Boniface Sindala',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'bonifacethesaint@gmail.com',
    'version' : '0.1',
    'intall_requires' : ['nose'],
    'packages' : ['GameOfCountries'],
    'scripts' : [],
    'name' : 'GameOfCountries'
]

setup(**config)
