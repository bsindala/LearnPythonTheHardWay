try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = [
    'description' : 'ex47',
    'author' : 'Boniface Sindala',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'bonifacethesaint@gmail.com',
    'version' : '0.1',
    'intall_requires' : ['nose'],
    'packages' : ['ex47'],
    'scripts' : [],
    'name' : 'ex47'
]

setup(**config)
