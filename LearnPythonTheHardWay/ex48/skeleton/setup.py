try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = [
    'description' : 'lexicon',
    'author' : 'Boniface Sindala',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'bonifacethesaint@gmail.com',
    'version' : '0.1',
    'intall_requires' : ['nose'],
    'packages' : ['ex48'],
    'scripts' : [],
    'name' : 'ex48'
]

setup(**config)
