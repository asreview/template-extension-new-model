from setuptools import setup
from setuptools import find_packages

setup(
    name='asreview-template-model-extension',
    version='0.1',
    description='Example classifier extension',
    url='https://github.com/asreview/asreview',
    author='ASReview Core Development Team',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='~=3.6',
    install_requires=[
        'sklearn',
        'asreview>=0.13'
    ],
    entry_points={
        'asreview.models': [
            'nb_example = asreviewcontrib.models.nb_default_param:NaiveBayesDefaultParamsModel',
        ],
        'asreview.feature_extraction': [
            # define feature_extraction algorithms
        ],
        'asreview.balance_strategy': [
            # define balance_strategy algorithms
        ],
        'asreview.query_strategy': [
            # define query_strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/asreview/issues',
        'Source': 'https://github.com/asreview/asreview/',
    },
)
