from codecs import open as op
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with op(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='re101',
    description='A back-pocket regex cookbook',
    long_description=long_description,
    version='0.2.0',
    author='Brad Solomon',
    author_email='brad.solomon.1124@gmail.com',
    url='https://github.com/bsolomon1124/re101',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Linguistic'
        ],
    keywords=[
        'regex',
        're',
        'tokenizer',
        'token',
        ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=3'
    )
