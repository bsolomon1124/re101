import codecs
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='re101',
    description='A back-pocket regex cookbook',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3.5',
    author='Brad Solomon',
    author_email='brad.solomon.1124@gmail.com',
    url='https://github.com/bsolomon1124/re101',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python :: Implementation :: CPython',
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
